a=[[1,2,3],[4,5,6]]   #2D list

b=a[0]
print(b)     
print(len(a))
for rows in a:
    for column in rows:
        print(column,end=' ')
    print()