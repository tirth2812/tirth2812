import csv #csv==coma seperated value 
#it is a file formet used to store tebuler data(database)
#write into csv file can be done using write row method and write rows methods
# the csv can be created using 'csv.writer' class  (or)    'csv.DictWriter'
#syntec for 'csv.writer' class == csv.writer(csv_file),dialect='excel',**fmtparams(formating parameters)
#csvfile=fileobject  with write method
#dialect(optional)=bydefault(excel)
#fmtparams=used formating parameters
#next line after filling the row 
with open('profiles1.csv', 'w', newline='') as file:

    writer = csv.writer(file) #writer and DictWriter
    field = ["name", "age", "country"]
    
    writer.writerow(field)
    writer.writerow(["Oladele Damilola", "40", "Nigeria"])
    writer.writerow(["Alina Hricko", "23", "Ukraine"])
    writer.writerow(["Isabel Walter", "50", "surat"])
    