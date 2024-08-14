#read date from user and print weekday of that date
import datetime
A=int(input('Enter the year:'))
for i in range(1,13):
    if (i in [1, 3, 5, 7, 8, 10, 12]):
        days=31
    elif (i in [4, 6, 9, 11]):
        days=30
    elif i == 2:
        if (A%4==0 and A%100!=0) or (A % 400 == 0):
            days= 29
        else:
            days= 28
    
    for j in range(1,days+1):
        date=datetime.date(A,i,j)
        if(date.weekday()==6):
            print(date)
    






            
            


    




        
    
    
    
    
    






