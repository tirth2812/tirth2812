import min_module
import max_module
a=int(input('enter value 1:'))
b=int(input('enter value 2:'))
if(a==b):
    print('both values are equal')
else:
    print('minimum is ',min_module.minimum(a,b))
    print('maximum is ',max_module.maximum(a,b))

