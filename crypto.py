from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import datetime

### CONFIG ###########
finalFile = 'final.csv'
currencies = ["BTC", "ETH", "LINK", "XTZ", "FIL", "VET", "STORJ", "XVG", "DOGE"]
####################


symbols = ""
for c, name in enumerate(currencies):
    if c > 0:
        symbols += ","
    symbols += name

#check for key file
try:
    f = open("key",'r')
    key = f.readline().rstrip()
except FileNotFoundError:
    print("Key file is missing. Please place file 'key' within the same directory as the script.")
    quit()


### DONT CHANGE ####

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {
  'symbol':symbols#'BTC,ETH,LINK,XTZ,FIL,VET,STORJ,XVG,DOGE'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': key,
}

session = Session()
session.headers.update(headers)
#####################

##### Check if CSV file exists #####
try:
    f = open(finalFile)
    f.close()
except FileNotFoundError:
    print('File does not exist. Creating a new one.')
    f = open(finalFile,'w')
    f.write("Time;")
    for c in currencies:
        f.write(c+";")
    f.write("\n")



###### Magic

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  final = open(finalFile,'a')
  final.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
  #### Iterate over all currencies
  for i in currencies:
    price = data["data"][i]["quote"]["USD"]["price"]
    final.write(";")
    ### Formatting, decimal places
    if price > 100:
        final.write(str(float("{:.1f}".format(price))))
    elif price > 10:
        final.write(str(float("{:.2f}".format(price))))
    elif price > 0.1:
        final.write(str(float("{:.2f}".format(price))))
    elif price > 0.001:
        final.write(str(float("{:.4f}".format(price))))
    else:
        final.write(str(price))
  final.write("\n")
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)