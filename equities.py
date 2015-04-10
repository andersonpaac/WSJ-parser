__author__ = 'andersonpaac'
import random
import logging
#@dev
SENTINEL=random.randint(-100,-1)  + 0.0         #Float Sentinel
STR_SENT = "UNSET"                              #String Sentinel

class Stock:
    price=SENTINEL
    symbol=STR_SENT
    chg_value = SENTINEL
    percent_chg = SENTINEL
    volume = SENTINEL
    csvd = STR_SENT
    def makecsv(self):
        csvd=str(self.symbol)+", "+str(self.price)+", "+str(self.chg_value)+", "+str(self.percent_chg)+", "
        csvd=csvd+str(self.volume)
        return csvd
    def logsentinal(self):
        logging.DEBUG("Sentinel value was set to "+str(SENTINEL))