#operation on list
l=[]
print(l)          #op=[]  # create empty list
l.append(6)       #append=to add element
l.append(10)      #append to add element
print(l)          #op=[6,10]

l.insert(1,7)     #(1,7) where 1 is index and 7 is number which is been added
print(l)          #[6,7,10]

l.reverse()       #reverse element in the list
print(l)          #op=[10,7,6]

l.sort()          #assending (by default)
print(l)          #op=[6,7,10]

l.sort(reverse=True)   #decending ==  (reverse=true)
print(l)               #op=[10,7,6]

l.remove(10)      #remove specific element
print(l)          #op=[7,6]

k=min(l)          #to find minimum value
print(k)          #op=6

k=max(l)          #to fin maximum
print(k)          #op=7

p=l.count(6)     #to count repetition of specific element in list
print(p)         #op=1

l.clear()        #to clear all element from list
print(l)         #op=[]

