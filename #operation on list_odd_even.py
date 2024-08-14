n=int(input('enter value'))
list=[]
for i in range(n):
    x=int(input())
    list.append(x)
print(list)
even_count=0
odd_count=0
for num in list:
    if(num%2==0):
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print(even_count)
print(odd_count)