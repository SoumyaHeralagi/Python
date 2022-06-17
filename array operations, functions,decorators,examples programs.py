#entering val

from array import *
arr=array('i',[])
n=int(input("enter the length"))
for i in range(n):
    x=int(input("enter a val"))
    arr.append(x)

print(arr)

#searching val

val=int(input("enter a val to search"))
for e in arr:
    if e==val:
        print(arr.index(val))
        break

# array operations

from numpy import *
arr1=array([2,6,8,1,3])
arr1=arr1+5
print(arr1)

a=array([1,2,3,4,5])
b=a.view()
print(a)
print(b)
a[1]=6
print(a)
print(b)


x=array([4,5,6,7,8])
y=x.copy()
print(x)
print(y)
x[4]=12
print(x)
print(y)


#functions


def greet():
    print("hello")
    print("good morning")

greet()


def add(x,y):
    c=x+y
    print(c)

add(5,7)


def average(n1,n2,n3):
    avg=(n1+n2+n3)/3
    print(avg)

average(3,4,8)


def update(x):
    x=8
    print(x)

update(10)


#varaible length arguments

def sum(a,*b):
    c=a
    for i in b:
        c=c+i
    print(c)

sum(5,6,34,78)


def person(name,*data):
    print(name)
    print(data)

person('navin',28,'mumbai',9865432)

#keyworded variable length arguments

def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,":",j)

person('navin',age=28,city='mumbai',mob=9865432)
    
#to count even and odd numbers in a list, passing list

def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    print("even :",even,"and odd :",odd)
lst=[23,45,64,22,68,77,9,44,83,82,98]
count(lst)

#fibonacci series

def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        if c<100:
            print(c)

fib(100)

#factorial

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)

x=5
res=fact(x)
print(res)

#recursion factorial


def fact(n):
    if n==0:
        return 1
    return  n*fact(n-1)
    

res=fact(5)
print(res)

#anonymous functions

f=lambda a:a*a
print(f(9))

#filter,map,reduce

from functools import reduce
nums=[2,4,6,8,4,6,2,9]
evens=list(filter(lambda n:n%2==0,nums))
doubles=list(map(lambda n:n*2,nums))
sum1=reduce(lambda a,b:a+b,nums)
print(evens)
print(doubles)
print(sum1)

#decorators

def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div=smart_div(div)
div(2,4)





      




