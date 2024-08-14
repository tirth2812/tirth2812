with open(r"E:\pythonprogramming\python\myfile3.txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:',lines)
search_text = "dummy"

replace_text = "mummy"
  
with open(r'E:\pythonprogramming\python\SampleFile.txt', 'r') as file: 
  
    data = file.read() 
  
    # Searching and replacing the text 
    data = data.replace(search_text, replace_text) 
  
# Opening our text file in write only 
with open(r'E:\pythonprogramming\python\SampleFile.txt', 'w') as file: 
     
    file.write(data) 
      
# Printing Text replaced 
print("Text replaced")    