Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

#operators

2+3
5
9-8
1
9+7
16
8*7
56
8/4
2.0
8//4
2
8+12-3
17
8+12-3
17
2*2
4
2**2
4

#printing 

print('navin laptop')
navin laptop
print("navin's laptop")
navin's laptop
print('navin's laptop')
      
SyntaxError: unterminated string literal (detected at line 1)
print("navin's laptop")
      
navin's laptop
print('navin's "laptop"')
      
SyntaxError: unterminated string literal (detected at line 1)
print('navin\s "laptop"')
      
navin\s "laptop"
print('navin\'s "laptop")
      
SyntaxError: unterminated string literal (detected at line 1)
print('navin\'s "laptop"')
      
navin's "laptop"
'navin '+'navin'
      
'navin navin'
'navin'*5
      
'navinnavinnavinnavinnavin'
print('c:\docs\navin')
      
c:\docs
avin
print(r'c:\docs\navin')
      
c:\docs\navin
7+7
      
14
x=3
      
x+3
      
6
y=3
      
x+y
      
6
x=9
      
x+y
      
12
x+y
      
12
y=7
      
x+y
      
16
x+10
      
19
_+y
      
26
name='youtube'
      
name
      
'youtube'
name+'rocks
      
SyntaxError: unterminated string literal (detected at line 1)
name+'rocks'
      
'youtuberocks'
name[0]
      
'y'
name[8]
      
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    name[8]
IndexError: string index out of range
name[6]
      
'e'
name[-1]
      
'e'
name[-2]
      
'b'
name[1:4]
      
'out'
name[1:]
      
'outube'
name[:]
      
'youtube'
'my '+name[3:]
      
'my tube'
myname='soumya heralagi'
      
len(myname)
      
15
nums=[25,12,36,95,14]
      
nums
      
[25, 12, 36, 95, 14]
nums[0]
      
25
nums[-1]
      
14
nums-[2:1]
      
SyntaxError: invalid syntax
nums[2:1]
      
[]
nums[2:]
      
[36, 95, 14]
nums[-5]
      
25
names=['soumya','sharat','madhu']
      
names
      
['soumya', 'sharat', 'madhu']
values=[9.5,'navin',25]
      
values
      
[9.5, 'navin', 25]
mil=[nums,names]
      
mil
      
[[25, 12, 36, 95, 14], ['soumya', 'sharat', 'madhu']]
mil1=[nums,names,values]
      
mil
      
[[25, 12, 36, 95, 14], ['soumya', 'sharat', 'madhu']]
mil1
      
[[25, 12, 36, 95, 14], ['soumya', 'sharat', 'madhu'], [9.5, 'navin', 25]]
nums.append(45)
      
nums
      
[25, 12, 36, 95, 14, 45]
nums.insert(2,12)nums
      
SyntaxError: invalid syntax
nums.insert(2,12)
      
nums
      
[25, 12, 12, 36, 95, 14, 45]
tup=(21,36,14,25)
      
tup
      
(21, 36, 14, 25)
tup[1]
      
36
s={22,25,14,21,5}
      
s
      
{5, 21, 22, 25, 14}
s
      
{5, 21, 22, 25, 14}
s={3,5,7,8,9,5}
      
s
      
{3, 5, 7, 8, 9}
s.difference(2)
      
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    s.difference(2)
TypeError: 'int' object is not iterable
s.difference('2')
      
{3, 5, 7, 8, 9}
s.difference('5')
      
{3, 5, 7, 8, 9}
help('keywords')
      

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
len(keyword.kwlist)
35
n=10
print(type(n))
<class 'int'>
spam = {'name': 'Pooka', 'age': 5} 

spam.setdefault('name','blue') 

print(spam)
SyntaxError: multiple statements found while compiling a single statement
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('name','blue')
'Pooka'
print(spam)
{'name': 'Pooka', 'age': 5}
spam[0]
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    spam[0]
KeyError: 0
spam[1]
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    spam[1]
KeyError: 1
spam[pooka]
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    spam[pooka]
NameError: name 'pooka' is not defined
spam[5]
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    spam[5]
KeyError: 5
spam
{'name': 'Pooka', 'age': 5}
data={'sou':'pam','viru':'anu','ran':'deep'}
print(data)
{'sou': 'pam', 'viru': 'anu', 'ran': 'deep'}
data[1]
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    data[1]
KeyError: 1
data['pam']
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    data['pam']
KeyError: 'pam'
data['sou']
'pam'
data['ran']
'deep'
data.keys()
dict_keys(['sou', 'viru', 'ran'])
data.values()
dict_values(['pam', 'anu', 'deep'])
data.values(1)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    data.values(1)
TypeError: dict.values() takes no arguments (1 given)
data.items()
dict_items([('sou', 'pam'), ('viru', 'anu'), ('ran', 'deep')])
data.items()[0]
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    data.items()[0]
TypeError: 'dict_items' object is not subscriptable
list(data.items())[0]
('sou', 'pam')
num=6+9j
type(num)
<class 'complex'>
data.get('viru')
'anu'
list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(2,10,2))
[2, 4, 6, 8]
list(range(20,3))
[]
list(range(1,20,3))
[1, 4, 7, 10, 13, 16, 19]
a=10
b=float(a)
b
10.0
a+b
20.0
c=a+b
c
20.0
c=int(c)
c
20
x=2
y=3
x+y
5
x-y
-1
a>b
False
a==b
True
a<=b
True
a>=b
True
a!=b
False
bin(25)
'0b11001'
0b0101
5
oct(25)
'0o31'
hex(25)
'0x19'
0xf
15
15
15
