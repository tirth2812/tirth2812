# roll_no, Name, City - csv

import csv

with open('students_d.csv', mode='w', newline='') as students_list:
    S_List = csv.writer(students_list)
    field_names = ["Roll_no", "Name", "City"]
    
    S_List.writerow(field_names)
    S_List.writerow(["1", "Dev", "Electical"])
    S_List.writerow(["2", "Milan", "Computer"])
    S_List.writerow(["3", "Nilay", "Electrical"])
    S_List.writerow(["4", "Tirth", "Computer"])


with open('students_d.csv', mode='r') as st_data:
    dt = csv.DictReader(st_data)                 # read from CSV file
    
    for row1 in dt:
        print(row1["Name"])