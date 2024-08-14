class Person:  
    def __init__(self, name, age):  #__init__refered as a constructor
        self.name = name    
        self.age = age      
    def greet(self):  
        print("Hello, my name is " ,self.age)  
        print("Hello, my age is " ,self.age) 
# Create a new instance of the Person class and assign it to the variable person1  
person1 = Person('Ayan',25)  
person1.greet()