#Change the description and other help messages here
def getdescription():
    descript="Program to decode WSJ's HTML page and return a CSV file"
    descript=descript+"that has a symbol,Price,%change,Volume"
    descript=descript+"The url can be found at "
    url="http://online.wsj.com/mdc/public/page/2_3021-gainnyse-gainer.html?mod=mdc_uss_pglnk"

    #Arguments help
    logtohelp="Set configlog file here\nExample usage main.py -l lfile.txt"

    sourcehelp="Set the source HTML file to be read here.\nIf you do not provide one , the latest copy will be"
    sourcehelp=sourcehelp+"obtained from the WSJ at " + url + " and will be used as the source\nExample usage"
    sourcehelp=sourcehelp+"\npython main.py -s sample.HTML"

    levelhelp="Sets the configlog level Choose 1:DEBUG , 2:INFO , 3:WARN AND ABOVE Example python main.py -lvl 2"
    ohelp = "Sets the output file where csv is written to , if unset -csv is written to a default filename"
    return descript+url,logtohelp,sourcehelp,levelhelp,ohelp