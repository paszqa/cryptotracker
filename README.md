# General requirements
Crypto price reporting tool

- requires python3
- requires python packages: json, request, datetime 
- requires CoinMarketCap key to be present in "key" file within the same directory as the script

## crypto.py

- creates a CSV reports within the same dir - "final.csv" (with price history) and "newest.csv" (with only newest prices)
- list is customizable and uses symbols (short versions of coin name, ex. BTC, ETH) - configured within the script itself

## calculate.py

- requires 'portfolio.csv' within same dir formatted as
```
name;quantity;paid_USD
ETH;0.12;0
XTZ;1.65;7.05
FIL;0.055;4.70
LINK;0.39;11.72
VET;223;17.58
STORJ;4.243;11.72
XVG;297.53;0
```
- creates a CSV report within same dir - "profit.csv" 

# Final notes

Files which do the work:

```
crypto.py
calculate.py
```

Files which are required for the above to work:

```
key
portfolio.csv
```

Files created by the scripts:

```
final.csv
newest.csv
profit.csv
```
