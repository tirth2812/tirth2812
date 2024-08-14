class SCET_SU:
    
    cnt=0
    def __init__(self,a,b):
        
        self.x = a
        self.y = b
        
    def setValues(self):
        self.x1=input('enter value of x: ')
        self.y1=input('enter value of y: ')
        SCET_SU.cnt1=int(input('enter value pof cnt'))
        
    def getValues(self):
        
        print('value of x is :',self.x1)
        print('value of y is :',self.y1)
        
obj=SCET_SU(5,10)
obj.setValues()
obj.getValues()
print('value of cnt is: ',SCET_SU.cnt1)
        
    
        
        

