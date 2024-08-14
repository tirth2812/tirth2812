#read date from user and print weekday of that date
import datetime
def datefinder(year,month,date):
    b=datetime.date(year,month,date)
    dayoftheweek=b.weekday()
    if(dayoftheweek==0):
        print('monday')
    elif(dayoftheweek==1):
        print('tuesday')
    elif(dayoftheweek==2):
        print('wednesday')
    elif(dayoftheweek==3):
        print('thursday')
    elif(dayoftheweek==4):
        print('friday')
    elif(dayoftheweek==5):
        print('saturday')
    elif(dayoftheweek==6):
        print('sunday')

A=int(input('Enter the year:'))
B=int(input('enter the month: '))
C=int(input('enter date: '))

ans=datefinder(A,B,C)
