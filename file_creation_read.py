#file_object=open('file name',access_mode)
file1 = open("myfile.txt", "r")  #r==read  #r+==read and write  #w==write  #w+read and write  #a==append  #a+==append and read

#L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# \n is placed to indicate EOL (End of Line)
  #write==to write single line    #\n==indicate end of the line
print(file1.readlines())      #writelines==multiple line

file1.close()  # to change file access modes and save data 
