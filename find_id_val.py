def HowMany(ID,Val):
    lenof_list=len(list)
    count=0
    for j in range(0,lenof_list):
        if(Val==ID[j]):
            count=count+1
        else:
            pass
    if(count==0):
        print('not found in list ')
    else:
        print(Val,'founds',count,' times') 
    
    
list=[]    
A=int(input('enter total no of ID: '))
for i in range(0,A):
    x=int(input('enter ID: '))
    list.append(x)
ID1=int(input('enter the id that you want to found: '))
HowMany(list,ID1)

    