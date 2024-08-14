import csv #csv==coma seperated value 
#it is a file formet used to store tebuler data(database)
#write into csv file can be done using write row method and write rows methods
# the csv can be created using 'csv.writer' class  (or)    'csv.DictWriter'
#syntec for 'csv.writer' class == csv.writer(csv_file),dialect='excel',**fmtparams(formating parameters)
#csvfile=fileobject  with write method
#dialect(optional)=bydefault(excel)
#fmtparams=used formating parameters
#next line after filling the row 

with open('E:\pythonprogramming\python\csv_read.csv',mode= 'r') as file:

    csvFile = csv.reader(file) #writer and DictWriter
    for lines in csvFile:
        print(lines)
    

 