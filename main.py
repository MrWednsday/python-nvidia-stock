import json
import nvidia_sku
import threading
import time

import pprint

pp = pprint.PrettyPrinter(indent=4)

url = "https://api-prod.nvidia.com/direct-sales-shop/DR/products/locale/currency/SKU"
discordWebhook = "https://discordapp.com/api/webhooks/759793732072505404/ihZ6VnwvIslhFUQuozaEYSKzBi5j4Th0owC-8tVPsgvrMH6MYYtZAdL9jRaKr_ZA1teG"

with open("config/config.json") as json_file:
    data = json.load(json_file)

#for region in data:
#    location = list(region)[0]
#    for model in list(region[location]["SKULIST"]):
#        if region[location]["SKULIST"][model]["SKU"]:
#            sku = region[location]["SKULIST"][model]["SKU"]
#            locale = region["Locale"]
#            curr = region["Currency"]
#
#            thread = threading.Thread(target=nvidia_sku.getSkuInfo, args=(url, discordWebhook, locale, curr, sku))
#            thread.start()
#            time.sleep(1)





nvidia_sku.getSkuInfo(url, discordWebhook, "en_gb", "GBP", "5438792800")
