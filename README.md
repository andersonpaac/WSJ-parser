#What it does
This program scrapes off data from the Wall Street Journals' top gainers' page and provide the output as a csv file.
The csv file has the symbols , price , change , percentage change , volume. WSJ updates the top gainers frequently 
through the day. This data could be helpful in any sort of financial analysis. 



#Usage
This will create a log file for you and a csv file , since no arguments are parsed , this would retrieve the 
current top gainers from [WSJ](http://online.wsj.com/mdc/public/page/2_3021-gainnyse-gainer.html?mod=mdc_uss_pglnk "Title") 
and will use that data as the source.
```
    python main.py
 ``` 
 If you'd like to give your own source consider using the -s tag , specifying the location of the HTML page as value
 ```
    python main.py -s sample.HTML
 ```
 Location of the output file can also be given with the -o tag and the log destination file can be provided with -l
 optionally the level of logging can be determined by the -lvl field. Please type the below command for help and 
 other information.
 ```
    python main.py -h 
 ```
 A sample command is given below this would parse sample.HTML as the source and log to loghere.txt and write the CSV file
 to sampleout.csv , logging would be done with lvl 2(0)- INFO level logging.
 ```
    python main.py -s sample.HTML -l loghere.txt -lvl 2 -o sampleout.csv 
 ```

