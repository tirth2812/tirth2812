#This is code to replace word in file

search_text = "This"

replace_text = "That"

with open(r'E:\pythonprogramming\python\file read.txt', 'r') as file: 

    data = file.read() 
    
    # Searching and replacing the text 
    data = data.replace(search_text, replace_text) 
  
# Opening our text file in write only 
with open(r'SampleFile.txt', 'w') as file: 

    file.write(data) 
  
# Printing Text replaced 
print("******Text replaced*******")
