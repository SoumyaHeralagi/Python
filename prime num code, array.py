#prime num

num=7
flag=False
if num>1:
    for i in range(2,10):
        if num%i==0:
            flag=True
            break

if flag:
    print("not prime")
else:
    print("prime")


#array


import array 
vals=array.array('i',[5,8,9,4,2])
print(vals)
print(vals.buffer_info())
print(vals.typecode)
print(vals.reverse())
print(vals[0])
for i in range(5):
    print(vals[i])


#2

from array import *
vals=array('i',[5,9,8,4,2])
newArr=array(vals.typecode,a*a for a in vals)
for e in newArr:
    print(e)

      
