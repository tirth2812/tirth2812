class box:
    l=10
    type='hard'
    def __init__(self,t,tl=30):
        self.type=t
        self.l=tl
    def disp(self):
        print(self.type,box.type)
        print(self.l,box.l)

b1=box('soft',20)
b1.disp()
box.type='flexi'
b2=box('hard')
b2.disp()