import random
heights=[10,20,30,40,50]
beg=random.randint(0,2)
end=random.randint(2,4)
print(beg)
print(end)
for x in range(beg, end):
    print(heights[x],end='@')
    