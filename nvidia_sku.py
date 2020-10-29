import notification
import requests
import json
import helpers
import time
import log

from datetime import datetime


def getSkuInfo(url, webhook, locale, currency, sku):
    timeCalled = 0

    notInStock = "PRODUCT_INVENTORY_OUT_OF_STOCK"
    inStock = "PRODUCT_INVENTORY_IN_STOCK"

    productId = None
    productName = None
    timeStart = None
    timeEnd = None

    apiDownNotification = False

    localUrl = url.replace("locale", locale).replace("currency", currency).replace("SKU", sku)
    
    response = requests.get(localUrl)
    timeCalled += 1

    if response.status_code == 200:
        json_r = response.json()
        productId = json_r["products"]["product"][0]["id"]
        productName = json_r["products"]["product"][0]["name"]

        time.sleep(helpers.time_delay())

        while True:
            response = requests.get(localUrl)

            if response.status_code == 200:

                apiDownNotification = False

                json_r = response.json()

                if json_r["products"]["product"][0]["inventoryStatus"]["status"] == inStock:
                    if timeStart == None:
                        timeStart = datetime.now()
                        notification.on_sale(webhook, productName, timeStart, productId)
                        log.response(localUrl, productName, json_r)

                if notInStock == json_r["products"]["product"][0]["inventoryStatus"]["status"]:
                    if timeStart != None:
                        timeEnd = datetime.now()
                        notification.time_on_sale(webhook, productName, timeStart, timeEnd)
                        timeStart = None
    
            elif response.status_code == 504:
                if not apiDownNotification:
                    apiDownNotification = True
                    notification.api_down(webhook, localUrl)
            
            time.sleep(helpers.time_delay())
    else:
        notification.api_error(webhook, localUrl)