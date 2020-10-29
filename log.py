from datetime import datetime
import os
import pprint

pp = pprint.PrettyPrinter(indent=4)

def response(url, productName, json):
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    productName = productName.replace(" ", "_").replace("/", "-")
    filename = "logs/" + date + "_" + productName.replace(" ", "_") + ".txt"
    f = open(filename,"w+")
    f.write(pp.pformat(json))
    f.close()
