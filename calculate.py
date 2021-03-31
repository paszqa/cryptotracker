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
f = open(path+"/portfolio.csv",'r')
g = open(path+"/newest.csv",'r')
p = open(path+"/profit.csv",'w')
p.write("ID;Coin name;Quantity;Bought for;Current price;Profit\n")
lines = f.readlines()[1:]
newestlines = g.readlines()[1:]
totalspent = 0
totalworth = 0
for (number, line) in enumerate(lines):
    #print(line.rstrip())
    splitline = line.split(";")
    name = splitline[0].rstrip()
    quantity = formatvalue(splitline[1].rstrip())
    boughtfor = formatvalue(splitline[2].rstrip())
    totalspent += float(boughtfor)
    p.write(str(number)+";"+name+";"+quantity+";"+boughtfor+";")
    #print(str(number)+" - "+name+" I have:"+quantity+" bought for "+boughtfor+ " now it costs: ")
    #find newest line with name
    for n in newestlines:
        splitnewest = n.split(";")
        if splitnewest[0] == name:
            worth = float(splitnewest[1]) * float(quantity)
            worth = twodecimal(worth)
            totalworth += float(worth)
            profit = float(worth) - float(boughtfor)
            profit = twodecimal(profit)
            p.write(str(worth)+";"+str(profit)+"\n")
            #print(str(worth)+" (single coin: "+splitnewest[1]+")")
totalprofit = float(totalworth) - float(totalspent)
totalprofit = twodecimal(totalprofit)
totalworth = twodecimal(totalworth)
totalspent = twodecimal(totalspent)
p.write("TOTAL;;;"+totalspent+";"+totalworth+";"+totalprofit+"\n")
f.close()
g.close()


