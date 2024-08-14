#quation1= write a python function calculatior that performs addition
#and subtraction,multiplication ,division of two perameters and  returns
#their results.

def calculator(x,y,ch):
    
    if(ch==1):
        return(x+y)
    elif(ch==2):
        return(x-y)
    elif(ch==3):
        return(x*y)
    elif(ch==4):
        return(x/y)
    else:
        print('enter valid choice')
        
perameter1=int(input('enter value of perameter 1:'))
perameter2=int(input('enter value of perameter 2:'))
choise=int(input('enter your choise:'))
ans=calculator(perameter1,perameter2,choise)
if(choise>=1 and choise <=4):
   print('your answer is ',ans)