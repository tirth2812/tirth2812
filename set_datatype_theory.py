##set datatype    
s1={4,10,72,20}
print(s1)

#print(s1[0])    error bcz unorder

s={4,10,72,20,10}
print(s)     #it remove copy(DUPLICATE NUMBER)

s3={1,2,3,4}
s4={1,2,3,4}
union_set=s3 | s4    #yog gan(union)
print(union_set)     #op={1,2,3,4,5,6,7,8}
print('-------------------------------------')
inter_set=s3&s4      #ched gan(intersection)
print(inter_set)     #op=set(1,2,3,4)
print('********************************')
diff_set=s3-s4        #difference btween 2 set 
print(diff_set)       #op={}
print('-------------------------------------')
diff_set=s3^s4      #common wil be elemnated
print(diff_set)     #op={}



 
