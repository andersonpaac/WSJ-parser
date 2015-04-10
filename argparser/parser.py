__author__ = 'andersonpaac'
import argparse
import helpers.descriptions as help

def args():
    descript,lhelp,shelp,lvlhelp,ohelp = help.getdescription()
    parser=argparse.ArgumentParser(description=descript)
    parser.add_argument("-l","--logto",help = lhelp,default="Unset")
    parser.add_argument("-s","--source",help = shelp,default="Unset")
    parser.add_argument("-lvl","--level",help = lvlhelp,default="1")
    parser.add_argument("-o","--output",help = ohelp,default="Unset")
    return parser
