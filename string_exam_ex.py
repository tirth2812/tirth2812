def makenew(mystr):
    newstr=''
    count=0
    for i in mystr:
        if count%2 != 0:
            newstr = newstr + str(count)
        else:
            if i.islower():
                newstr = newstr + i.upper()
                print("new string is: ",newstr)
                print("################################")
            else:
                newstr = newstr + i
                print("new else string is: ",newstr)
                print("********************************")
        count += 1
        newstr = newstr + mystr[:1]
        print("new string 1 is: ",newstr)

makenew("sTUdeNT")