from discord_webhook import DiscordWebhook
from datetime import datetime


def api_error(webhookUrl, url):
    message = "API Error \nURL used: " + url
    webhook = DiscordWebhook(url=webhookUrl, content=message)
    webhook.execute()


def start_api_check(webhookUrl, productId, productName, productStatus):
    message = "API check Started\n\tProduct ID: " + str(productId) + "\n\tProduct Name: "
    message += productName + "\n\tProduct Status: " + productStatus
    webhook = DiscordWebhook(url=webhookUrl, content=message)
    webhook.execute()

def api_down(webhookUrl, url):
    message = "API Down\n\tStatus code: 504\n\tURL used: " + url
    webhook = DiscordWebhook(url=webhookUrl, content=message)
    webhook.execute()

def on_sale(webhookUrl, productName, saleStart, sku):
    message = "<@&760951058930991104>\n\tProduct on Sale: " + productName + "\n\tSale start: " + saleStart.strftime("%Y/%m/%d - %H:%M:%S") + "\n\tSKU: " + str(sku)
    webhook = DiscordWebhook(url=webhookUrl, content=message)
    webhook.execute()

def time_on_sale(webhookUrl, productName, saleStart, saleEnd):
    message = "Product not longer on sale" + "\n\tProduct Name" + productName
    message += "\n\tSale start: " + saleStart.strftime("%Y/%m/%d - %H:%M:%S")
    message += "\n\tSale end: " + saleEnd.strftime("%Y/%m/%d - %H:%M:%S")
    message += "\n\tTime on sale: " + str(saleEnd - saleStart)
    webhook = DiscordWebhook(url=webhookUrl, content=message)
    webhook.execute()