__author__ = 'andersonpaac'
import argparse
import helpers.descriptions as help

def args():
    descript,lhelp,shelp,lvlhelp = help.getdescription()
    parser=argparse.ArgumentParser(description=descript)
    parser.add_argument("-l","--logto",help = lhelp,default="logger.log")
    parser.add_argument("-s","--source",help = shelp)
    parser.add_argument("-lvl","--level",help = lvlhelp,default="1")
    return parser
