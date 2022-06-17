Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

#swaping using temp var

a=5
b=6

temp=a
a=b
b=temp
print(a)
6
print(b)
5

#swaping without temp var

a=9
b=8
a=a+b
b=a-b
a=a-b
print(a)
8
print(b)
9

swping using bit operator

a=4
b=7
a=a^b
b=a^b
a=a^b
print(a)
7
print(b)
4

swaping without any operators

a=3
b=6
a,b=b,a
print(a)
6
print(b)
3

#compliment
~12
-13

#and

12&13
12

#or

12|13
13

#and

25&30
24

#xor

20^14
26

#lefy shift

10<<2
40

#importing math

import math
x=sqrt(25)

import math
x=math.sqrt(25)
x
5.0
print(math.floor(2.9))
2
print(math.ceil(2.1))
3
print(math.pow(3,2))
9.0

import math as m
m.sqrt(36)
6.0


from math import sqrt, pow
pow(4,5)
1024.0


#prime or not

num=7
for i in range(2,10):
    if num%i==0:
        print("not prime")
else:
    print("prime")





