import csv 

with open('student_data.csv', 'w', newline='') as file:

    write = csv.writer(file) #writer and DictWriter
    field = ["name", "roll no", "city"]
    
    write.writerow(field)
    write.writerow(["tirth", "40", "surat"])
    write.writerow(["dev", "23", "surat"])
    write.writerow(["milan", "50", "surat"])
    
with open('student_data.csv',mode='r',newline='') as file1:
        
        read = csv.reader(file1)
        for lines in read:
            print(lines)
        