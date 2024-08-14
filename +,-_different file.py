# Write a python program to read data from “file1.csv”, if data is 
# negative write it in “negative.csv” and if data is positive write it 
# in “positive.csv

import pandas as pd
import csv

data = pd.read_csv('numbers1.csv')
# print(data.Values)
with open('negative.csv', mode='w', newline='') as val_sorting:
    S_List = csv.writer(val_sorting)
    field_names = ["Negative_Values"]
    S_List.writerow(field_names)
    
    for row in data.number:
        if( row < 0 ):
            S_List.writerow([row])

with open('positive1.csv', mode='w', newline='') as val_sorting:
    S_List = csv.writer(val_sorting)
    field_names = ["Positive_Values"]
    S_List.writerow(field_names)

    for row in data.number:
        if( row >= 0 ):
            S_List.writerow([row])