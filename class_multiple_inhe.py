class gtu:  
     
    def GTU(self):  
      print('your name is ',self.name)
                
class  su:
    
    def SU(self):
        print('your name is ',self.name)
               
class student(gtu,su):
    
    def __init__(self):
        self.name=input('enter your name is: ')
        
        
# Create a new instance of the Person class and assign it to the variable person1  
stu = student()  
stu.GTU()
stu.SU()
