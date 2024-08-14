class target:
    def __init__(self):
        self.x=20
        self.y=24
    def disp(self):
        print(self.x,self.y)
    def __del__(self):
        print('target moved')
        
def one():
    t=target()
    t.disp()
    
one()

