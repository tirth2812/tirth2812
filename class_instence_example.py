class Myclass:
    # Class variable
    #school_name = 'ABC School '
    
    def __init__(self):
        self.x = 10
        self.y = 20
        
    def setValues(self):
        self.x1=input('enter value of x: ')
        self.y1=input('enter value of y: ')
        
    def getValues(self):
        
        print('value of x is :',self.x1)
        print('value of y is :',self.y1)
        
obj=Myclass()
obj.setValues()
obj.getValues()
        
    
        
        

