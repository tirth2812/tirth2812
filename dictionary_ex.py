dict={1:'isha',2:'nisha',3:'anish'}
print(dict)
dict[4]='manisha'   #add
print(dict)

dict[3]='anisha'    #update
print(dict)
print('********')
dict.pop(3)     #remove
print(dict)

A=len(dict)   #length
print(A)

B=dict.get(1)   #get paticuler value
print(B)

B=dict.get(10)   #get paticuler value
print(B)

del(dict[1])    #remove 
print(dict)

dict.clear()     #clear
print(dict)