import csv 
with open('python_data.csv', 'w', newline='') as Python_Data:

    writer = csv.writer(Python_Data) #writer and DictWriter
    
    field = ["name", "mobile number", "branch"]
    
  
    writer.writerow(field)
    writer.writerow(["tirth", "5445454545", "EC"])
    writer.writerow(["dev", "1212121212", "CS"])
    writer.writerow(["milan", "7878787878", "CS"])
    writer.writerow(["nilay", "5656565656", "electrical"])
    