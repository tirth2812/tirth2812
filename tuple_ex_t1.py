##tuple datatype
t1=(4,10,72,20)  #list datatype is immutable
print(t1[1:3])   # ending=n-1

print(len(t1))   #4    #no of member
k=min(t1)        #minimum no
print(k)         #op=4
k=max(t1)        #maximum no
print(k)         #op=72

t2=(1,2,3,4)
print(t1+t2)

print(t1[::-1])  #op=(20,72,10,4)

print(t1*2)  #repeate t1 two times in same tuple
  ##membership operator
print(15 in t1)#op=false  #find particuler member in tuple

print(10 in t1)#op=true  #10 in tuple 

print(15 not in t1)



