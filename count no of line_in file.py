#count lines in file
num_lines = 0
 
with open("E:\pythonprogramming\python\file read.txt", 'r') as f:
    for line in f:
        lines = line.split("\n")
        num_lines += 1
print("Number of lines:")
print(num_lines)