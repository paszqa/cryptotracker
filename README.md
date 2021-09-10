# General requirements
Crypto price reporting tool

- requires python3
- requires python packages: json, request, datetime 
- requires CoinMarketCap key to be present in "key" file within the same directory as the script

# Simple how to

1. Install required packages

2. Generate your own API key from CoinMarketcap

3. Put this key in the same directory as the script, filename "key"

4. Create "portfolio.csv" file in the same directory with the list of your crypto purchases (formatting example shown below)

5. Execute crypto.py

6. Execute calculate.py

7. Results will be put in files in the same directory: final.csv, newest.csv, profit.csv, history.csv

8. (Optional) Schedule the execution a couple of times a day, with a reasonable pause between crypto.py and calculated.py (ex. with ~15 currencies tracked about 5 minutes should be enough for a RPi3 hardware)

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
- creates a CSV report within same dir - "history.csv" - which contains easy gains table to make graph creation faster

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
history.csv
```
