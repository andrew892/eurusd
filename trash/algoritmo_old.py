from datetime import datetime

MOVE = 10
EUR = 1000
USD = 0

buys = []
day = -1
first_bid = -1


def step(timestamp,bid):
    global day
    global first_bid
    global EUR
    global USD
    
    #verifica di cambio giorno
    data_day = datetime.fromtimestamp(float(timestamp)/1000.0).day
    if data_day != day:
        print("--- CAMBIO GIORNO {} ---".format(day))
        day = data_day
        first_bid = bid
    
    # acquisto
    if (bid > first_bid + 0.001 and len(buys) == 0) or (bid > first_bid + 0.0015 and len(buys) == 1):
        EUR -= MOVE
        USD += MOVE * bid
        buys.append(bid)
        print("{:11.6f} EUR - {:11.6f} USD - comprato a bid {:8.6f}".format(EUR,USD,bid))
    
    # vendita
    for buy in buys:
        if bid < buy - 0.0012:
            EUR += MOVE * buy / bid
            USD -= MOVE * buy
            buys.remove(buy)
            print("{:11.6f} EUR - {:11.6f} USD - venduto  a bid {:8.6f}".format(EUR,USD,bid))
    return None 

    
with open('eurusd.log','r+') as datafile:
    for line in datafile:
        _,timestamp,bid = line.strip().split(';')
        bid = float(bid) / 10000.0
        step(timestamp,bid)

with open('miniout.csv','r') as datafile:
    for line in datafile:
        date,_,_,_,bid,_ = line.strip().split(',')
        date = datetime.strptime(date,'%d.%m.%Y %H:%M:%S.%f')
        bid = float(bid)
        step(timestamp,bid)
