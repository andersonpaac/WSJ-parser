__author__ = 'andersonpaac'
import logging

#Sets configlog to WARNING level
def configLogger(depend=None,progname="prog"):
    fname=progname+".log"           #Set Defaults
    lvl=30                          #Default level of WARNING

    if(type(depend) is int):
        if(depend==1):
            message= "INFO: No log file is set\nPlease consider setting a log file destination with  the -l tag and log"
            message=message+ " level with -lvl Creating a temporary logfile "+str(progname)+" only "
            message=message+ "Info level actions and higher will be sent here(configlog.Info)"
            print message
            logging.basicConfig(filename=fname,level=lvl,format='%(levelname)s:%(message)s')

    else:

        try:
            fname=depend.logto
            try:
                lvl=int(depend.level)
                lvl=lvl*10
            except ValueError:
                msg= "WARN:Your value for -lvl is incorrect please choose an integer between 1 and 3 type python main.p"
                msg=msg+"y -h for help"
                print msg

            logging.basicConfig(filename=fname,level=lvl,format='%(levelname)s:%(message)s')

        except AttributeError:
            msg="INFO: You've not provided a logname to log to , this program will log to "+fname+" with a log level of "
            msg = msg + "WARNING"
            print msg
            logging.basicConfig(filename=fname,level=lvl,format='%(levelname)s:%(message)s')
