#file_object=open('file name',access_mode)
file2 = open("myfile2.txt", "w")  #r==read  #r+==read and write  #w==write  #w+read and write  #a==append  #a+==append and read
file1=open("myfile.txt","r")

A=file1.readlines()
# \n is placed to indicate EOL (End of Line)
 #write==to write single line    #\n==indicate end of the line
file2.writelines(A)      #writelines==multiple line
file2.close()  # to change file access modes and save data
file1.close()
