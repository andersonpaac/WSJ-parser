__author__ = 'andersonpaac'
'''
stage-1 :   Get arg parse commands : Complete
stage-2 :   Setup configlog        : Complete
stage-3 :   Service integration
stage-4 :   Actuals                : Tasking

'''
from time import sleep

import argparser.parser as arg
import configlog.logger as lg
import logging
import urllib2
from lxml import etree
from equities import Stock
import datetime
#@dev
progname="WSJ-parser"
url="http://online.wsj.com/mdc/public/page/2_3021-gainnyse-gainer.html?mod=mdc_uss_pglnk"


#returns the tree module
def clean(argg):
    if argg.source=="Unset":
        logging.info("Didn't set a URL to get from , getting the latest data")
        tree= getpage()
        return tree
    else:
        logging.info("A source file was given -"+argg.source)
        a=open(argg.source,"rb")
        data=a.read()
        tree=etree.HTML(data)
        a.close()
        return  tree
#Makes network access to WSJ to retrieve latest information
def getpage():
    try:
        ulib=urllib2.urlopen(url)
        tree=etree.HTML(ulib.read())
        logging.debug("URL Request made and successful")
        return tree
    except urllib2.URLError:
        logging.error("Network connection failed")
        print "failed to connect to the network , please try using the --source argument for giving an offline page"
        exit(-1)

def goget(argg):
    tree=clean(argg)
    symbols_raw = tree.xpath("//tr/td/a/text()")
    price_raw = tree.xpath("//tr/td[3]/text()") [1:-3]                  #Removing \n's and other data
    change_raw = tree.xpath("//tr/td[4]/text()")[1:]                    #Removing first element "CHG"
    percent_change_raw = tree.xpath("//tr/td[5]/text()")[1:]            #Removing %Chg
    volume = tree.xpath("//tr/td[6]/text()")[1:]

    if(len(symbols_raw) != len(price_raw) != len(change_raw) != len(percent_change_raw) != len(volume)):
        logging.critical("SANITY CHECK FAILED ERROR: Unsynchronized lengths\nBeginging variable dump---------")
        logging.critical("symbols_raw %s , \nprice_raw %s , \nchange_raw %s ",str(symbols_raw),str(price_raw),str(change_raw))
        logging.critical("percentage_change_raw %s , \nVolume %s",str(percent_change_raw),str(volume))
        errmsg = "An error has occured , please create an issue on the git repository at "
        errmsg = errmsg+"https://github.com/andersonpaac/WSJ-parser"
        print errmsg
    else:
        stocks=[]
        stock=Stock()
        stock.symbol=symbols_raw[0].split("(")[1].split(")")[0]
        stock.price = price_raw[0].split("$")[1]
        stock.chg_value = change_raw[0]
        stock.percent_chg = percent_change_raw[0]
        stock.volume = volume[0]
        stocks.append(stock)
        for i in xrange(1,len(symbols_raw)):
            stock=Stock()
            stock.symbol=symbols_raw[i].split("(")[1].split(")")[0]
            stock.price = price_raw[i]
            stock.chg_value = change_raw[i]
            stock.percent_chg = percent_change_raw[i]
            stock.volume = volume[i]
            stocks.append(stock)
            i = i + 1

        logging.info("Completed parsing")
        writetocsv(argg,stocks)

def writetocsv(argg,stocks):
    print len(stocks)
    fname=progname+"_"+str(datetime.datetime.now())[:-5]+".csv"
    if argg.output != "Unset":
        fname=argg.output
    logging.info("Initiating write to "+fname)
    writer = open(fname,"wb")
    for each in stocks:
        writer.write(each.makecsv()+"\n")
    writer.close()
    logging.info("Complete writing")
    print "Written to "+fname






def main():
    parser = arg.args()
    lg.configLogger(parser.parse_args(),progname)
    goget(parser.parse_args())
main()