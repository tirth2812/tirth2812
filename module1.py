#create a udm with simple function for addition ,substraction,multiplication and division
#write a program to input module an access function defined in the module
def ans(x,y,z):
    if(z=='+'):
        return(x+y)
    elif(z=='-'):
        return(x-y)
    elif(z=='*'):
        return(x*y)
    elif(z=='/'):
        return(x/y)
    else:
        return(print('wrong choice'))
    
