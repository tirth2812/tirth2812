class Person:  
    def __init__(self, length,width):  
        self.length = length    
        self.width = width
           
    def greet(self):  
        answer=self.length*self.width 
        print("area of rect is " ,answer)  
        
# Create a new instance of the Person class and assign it to the variable person1  
l=int(input('enter value of length: '))
w=int(input('enter value of width: '))
person1 = Person(l,w)  
person1.greet()