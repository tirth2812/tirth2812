#Given a point(x,y), Write Python Program to find whether this point
#lies in the First, Second, Third or Fourth Quadrant of X - Y Plane. Print 
#message of corresponding quadrant.

x=int(input('enter value of x: '))
y=int(input('enter value of y: '))

if(x>0 and y>0):
    print('point lie in first quadrant')
elif(x>0 and y<0):
    print('forth quadrant')
elif(x<0 and y<0):
    print('third quadrant')
elif(x<0 and y>0):
    print('second quadrant')
elif(x==0 and y==0):
    print('origin')
else:
    print('enter valid point')