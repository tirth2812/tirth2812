#write a program to calculate a% of student using multilevel inheritence
class cordination:  
        def __init__(self):
            self.length=int(input('enter length:'))
            self.width=int(input('enter width:'))
            
                
class  area(cordination):
     
     def calc(self):
            self.calculation=self.length*self.width
            print('aea of rect is ',self.calculation)
                  
class perimeter(cordination):
    
        def calc1(self):  
           self.calculation1=2*(self.length+self.width)
           print('pari of rect is: ',self.calculation1)
        
        
        
# Create a new instance of the Person class and assign it to the variable person1  
a1 = area()  
a1.calc()
p1 = perimeter() 
p1.calc1()