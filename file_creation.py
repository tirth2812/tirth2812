#file_object=open('file name',access_mode)
file1 = open("myfile.txt", "w")  #r==read  #r+==read and write  #w==write  #w+read and write  #a==append  #a+==append and read

L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")  #write==to write single line    #\n==indicate end of the line
file1.writelines(L)      #writelines==multiple line
file1.close()  # to change file access modes and save data