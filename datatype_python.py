# Data types....

a = 3       # integer
print(a)

b = 4.56    # float
print(b)

c = 3 + 4j  # complex
print(c, type(c))


#string dstatype
str1 = "hello"    # string
print(str1, str1[0:4], str1[-1])    # str[-1] = 'o' due to negative indexing.
print(str1[0:4])    # 0 to 3 = 'hell'


mystr = 'SCET is the best college'
print(mystr[15::1])     # t college
print(mystr[15::2])     # tclee
print(mystr[-10:-1:2])  # s olg
print(mystr[:5])        # SCET (with space at the end)
print(mystr[12:])       # best college
print(mystr[-4:-1])     # leg
print(mystr[-4:-1:-1])  # leg  = cant go to right side with (-1) step


#list datatype==enclosed with square bracket
list1 = [10, 'Red', 4.3]
print(list1, type(list1))
print(list1[1])#'Red'

#'tuple==collection of different datatype enclosed in round bracket'
tuple = (10, 'Red', 4.3)
print(tuple[1])
print(tuple,type(tuple))

#set== #it is collection on different data type enclosed by curly bracket
      #it is an unordered collection
      
set={10,'yellow',7.2}
#print(list1[1]) 
print(set,type(set))


#dictionary==it is collection of different data types in form of key:value pair
            #the element are enclosed in curly brackets
            
l1={1:'tirth','branch':'ec','country':'usa'}
print(l1.keys())
print(l1['country'])
print(l1['branch'])

#boolian==it provides two values true or false
x=5
y=10
print(bool(x==y))
print(bool(x!=y))
