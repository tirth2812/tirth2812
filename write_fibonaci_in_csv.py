# roll_no, Name, City - csv
import pandas as pd
import csv

with open('fibonaci.csv', mode='w', newline='') as students_list:
    S_List = csv.writer(students_list)
    field_names = ["fibonaci"]
    
    S_List.writerow(field_names)
    a=0
    b=1
    count=0
    S_List.writerow([a])
    S_List.writerow([b])
    for i in range(1,10):
        
        c=a+b
            
        S_List.writerow([c])
        a=b
        b=c
        
        
        
    
    

