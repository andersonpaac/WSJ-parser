__author__ = 'andersonpaac'
'''
stage-1 :   Get arg parse commands
stage-2 :   Setup configlog
stage-3 :   Service integration

'''
from time import sleep

import argparser.parser as arg
import configlog.logger as lg

progname="WSJ-parser"

def main():
    parser = arg.args()
    lg.configLogger(parser,progname)

main()