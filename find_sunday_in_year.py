#read date from user and print weekday of that date
import datetime

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Function to get the number of days in a given month of a year
def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if leap_year(year):
            return 29
        else:
            return 28
        


A=int(input('Enter the year:'))
leap_year(A)
for i in range(1,13):
    days=days_in_month(A,i)
    
    for j in range(1,days+1,1):
        date=datetime.date(A,i,j)
        if(date.weekday()==6):
            print(date)
    






            
            


    




        
    
    
    
    
    






