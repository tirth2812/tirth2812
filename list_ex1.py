list1 = [ ]
inp = int(input("total elements "))
for i in range(inp):
 a = int(input("Enter the elements: "))
 list1.append(a)

length = inp
list2 = [ ]
for i in range(length):
    if(list1[i] not in list2):
        list2.append(list1[i])
print(list2)