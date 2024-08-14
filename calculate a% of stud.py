#write a program to calculate a% of student using multilevel inheritence
class marks:  
        def __init__(self):
            self.mark1=int(input('enter your no of subject:'))
            self.mark2=int(input('enter your no of subject:'))
            self.mark3=int(input('enter your no of subject:'))
                
class  per(marks):
     
     def calc(self):
            self.calculation=(self.mark1+self.mark2+self.mark3)/3
                  
class result(per):
        def perct(self):  
           print('your result is ',self.calculation)
        
        
        
# Create a new instance of the Person class and assign it to the variable person1  
stu = result()  
stu.calc()
stu.perct()