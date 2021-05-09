import pathlib
from datetime import datetime
def formatvalue(val):
    ### Formatting, decimal places
    val = float(val)
    if val > 100:
        return str(float("{:.1f}".format(val)))
    elif val > 10:
        return str(float("{:.2f}".format(val)))
    elif val > 0.1:
        return str(float("{:.2f}".format(val)))
    elif val > 0.001:
        return str(float("{:.4f}".format(val)))
    else:
        return str(val)

def twodecimal(val):
    val = float(val)
    return str(float("{:.2f}".format(val)))

path = pathlib.Path(__file__).parent.absolute()
f = open(str(path)+"/portfolio.csv",'r')
g = open(str(path)+"/newest.csv",'r')
p = open(str(path)+"/profit.csv",'w')
h = open(str(path)+"/history.csv",'a')

p.write("ID;Coin name;Quantity;Bought for;Current price;Profit\n")
lines = f.readlines()[1:]
newestlines = g.readlines()[0:]
totalspent = 0
totalworth = 0
totalinvestedthen = 0
totalinvestednow = 0
for (number, line) in enumerate(lines):
    #print(line.rstrip())
    splitline = line.split(";")
    name = splitline[0].rstrip()
    quantity = formatvalue(splitline[1].rstrip())
    boughtfor = formatvalue(splitline[2].rstrip())
    if float(boughtfor) > 0:
        totalinvestedthen += float(boughtfor)
    totalspent += float(boughtfor)
    p.write(str(number)+";"+name+";"+quantity+";"+boughtfor+";")
    #print("1:"+name)
    #print(str(number)+" - "+name+" I have:"+quantity+" bought for "+boughtfor+ " now it costs: ")
    #find newest line with name
    for n in newestlines:
        splitnewest = n.split(";")
        if splitnewest[0] == name:
            worth = float(splitnewest[1]) * float(quantity)
            if float(boughtfor) > 0:
              roi = (worth/float(boughtfor)) * 100
              roi = twodecimal(roi)
            else:
              roi = "---"
            worth = twodecimal(worth)
            totalworth += float(worth)
            profit = float(worth) - float(boughtfor)
            profit = twodecimal(profit)
            #roi = twodecimal(roi)
            #print("xyz-"+name)
            if float(boughtfor) > 0:
              totalinvestednow += float(worth)
            p.write(str(worth)+";"+str(profit)+"("+str(roi)+"%)"+"\n")
            #print(str(worth)+" (single coin: "+splitnewest[1]+")")
totalprofit = float(totalworth) - float(totalspent)
totalreturn = twodecimal(totalworth/totalspent * 100)
totalprofit = twodecimal(totalprofit)
totalworth = twodecimal(totalworth)
totalspent = twodecimal(totalspent)
#totalreturn = twodecimal(totalworth/totalspent * 100)
date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
p.write("TOTAL;"+date+";;"+totalspent+";"+totalworth+"("+totalreturn+"%)"+";"+totalprofit+"\n")
h.write(date+";"+str(totalinvestedthen)+";"+str(twodecimal(totalinvestednow))+";"+str(twodecimal(totalinvestednow - totalinvestedthen))+"\n")
f.close()
g.close()


