from datetime import datetime

MOVE = 10
EUR = 1000
USD = 0

buys = []
day = -1
first_bid = -1


def step(date,bid):
    global day
    global first_bid
    global EUR
    global USD
    
    #verifica di cambio giorno
    data_day = date.day
    if data_day != day:
        print("--- CAMBIO GIORNO {}/{} ---".format(date.day,date.month))
        day = data_day
        first_bid = bid
    
    # acquisto
    if (bid > first_bid + 0.001 + 0.0005*len(buys) and len(buys) < 20):
        EUR -= MOVE
        USD += MOVE * bid
        buys.append(bid)
        print("{:11.6f} EUR - {:11.6f} USD - comprato a bid {:8.6f} - quote {:2d}".format(EUR,USD,bid,len(buys)))
    # acquisto
#    if (bid > first_bid + 0.001 and len(buys) == 0) or (bid > first_bid + 0.0015 and len(buys) == 1):
#        EUR -= MOVE
#        USD += MOVE * bid
#        buys.append(bid)
#        print("{:11.6f} EUR - {:11.6f} USD - comprato a bid {:8.6f}".format(EUR,USD,bid))
    
    # vendita
    for buy in buys:
        if bid < buy - 0.0012:
            EUR += MOVE * buy / bid
            USD -= MOVE * buy
            buys.remove(buy)
            print("{:11.6f} EUR - {:11.6f} USD - venduto  a bid {:8.6f} - quote {:2d}".format(EUR,USD,bid,len(buys)))
    return None 

    
with open('out.csv','r') as datafile:
    for line in datafile:
        date,_,_,_,bid,_ = line.strip().split(',')
        date = datetime.strptime(date,'%d.%m.%Y %H:%M:%S.%f')
        bid = float(bid)
        step(date,bid)

print("---------------------------")
print("SIMULAZIONE TERMINATA:")
print("EUR: {}".format(EUR+USD/bid))
