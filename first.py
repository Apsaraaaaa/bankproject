name='Sharya'
age=24
mark=90
print(name)
print(type(name))
print(age)
print(type(age))
print(mark)
print(type(mark))
a=10
b=20
sum=a+b
print(sum)
sub=a-b
print(sub)
mul=a*b
print(mul)
div=a/b
print(div)
a=10
b=20
#print(not(a>b))
def Cal_sum(a,b):
    sum=a+b
    return sum
print(Cal_sum(5,10))
a=int(input('Enter first number'))
b=int(input('Enter second number'))
sum=a+b
print(sum)
#condition:if else
age=20
if age>=18:
    print('Eligible to vote')
else:
    print('Not eligible to vote')

Mark=80
if Mark>=90:
    print('A')
elif Mark>=80:
    print('B')
elif Mark>=70:
    print('C')
else:
    print('Fail')
    
#loop
i=1
while i<=5:
    print(i)
    i+=1

i=5
while i>=1:
    print(i)
    i-=1
    
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print('end')
    
#range
for i in range(5):
    print(i**2)
for i in range(1,10,2):
    print(i)
for i in range(0,10,2):
     print(i)
list=[20,30,90,'Ram']
print(list)
print(type(list))
list[0]=50
print(list)
list.append(80)
print('Hello')
list=[50,40,50]
list[0]=80
list.append(90) #last ma add hunxa
list.sort()
list.reverse()
print(list)
print(type(list))

#tupple:immutable hunxa
tup=(50,50,40)
print(tup.count(50))
print(len(tup))
print(tup.index(50))
print(tup)
print(type(tup))

#dictionary:key value ko pair
dict={
    'name':'Apsara',
    'age':21,
    'marks':[90,80,70]
}
dict['name']='Apsaraaaa'
print(dict)
print(type(dict))
print(dict['name'])

#set:unorder 
set1={1,2,2,3,'ram','gita'}
print(len(set1))
set1.add(9)
set1.remove(2)
set1.pop()
#set1.clear()
print(set1)

set1={1,2,3,4,5}
set2={1,2,7,8,5}
print(set1)
print(set2)
print(set1.intersection(set2))
print(set1.union(set2))
#frozen set:frezes
set1={1,2,2,3,4}
set2={2,4,5,6,7}
froset1=frozenset(set1)
froset2=frozenset(set2)
print(froset1)
print(froset2)
print(froset1.intersection(froset2))


from collections import deque
dq=deque([1,2,3,2,4,5])
dq.append(6)
dq.appendleft(0)
dq.remove(2)
#dq.extend(list)
dq.insert(2,20)
#dq.extendleft(list)
print(dq)

from collections import defaultdict
d=defaultdict(int)
d['a']+=1
print(d)

from collections import defaultdict
name='sitaram'
dd=defaultdict(int)
for ch in name:
    dd[ch]+=1
    print(dd)
    
#traditional way
squares=[]
for x in range(5):
    squares.append(x**2)
print(squares)

#list comprehnsion
squares=[x**2 for x in range(5)]
print(squares)

#dict comprenhension
d={x:x**2 for x in range(5)}
print(d)

#generators:A generator is a special type of iterator,instaead of storing all values in memory
gen=(x**2 for x in range(5))
for val in gen:
    print(val)
    
marks=[60,70,80,90]
def s_grade(marks):
    if marks>=90:
        return 'A'
    elif 90>marks>=80:
        return 'B'
    elif 80>marks>=70:
        return 'C'
    else:
        return 'D'
grade=map(s_grade,marks)
print('student marks',marks)
print("student grade",next(grade))
print("student grade",next(grade))
print("student grade",next(grade))
print("student grade",next(grade))


#filter
marks=[60,50,45,35]
def fail(marks):
    return marks<50
result=filter(fail,marks)
print('student marks',marks)
print('failing marks',list(result))

#reduce
from functools import reduce
num=[2,4,6,8]
def my_sum(x,y):
    return x+y
sum=reduce(my_sum,num)
print(sum)

#lamda
num=5
square=num**2
print('square is:',square)
f=lambda x: x**2
print(f(5))

#exception handle
try:
    num=int(input('Enter a number:'))
    result=10/num
    print('Result is:',result)
except ZeroDivisionError:
    print('Cnnot divide by zero')
except ValueError:
    print('Invalid input,please enter a number')


class NegativeValueError(Exception):
    pass
try:
    num=int(input('Enter a positive number:'))
    if num<0:
        raise NegativeValueError("Negative values not allowed")
    print('You enterered:',num)
except NegativeValueError as e:
    print(e)
except ValueError:
    print('Invalid input,please enter a valid number')
    
class Student:
    def data(self,name,age):
        self.name=name
        self.age=age
s1=Student()
s1.data('Ram',20)
s2=Student()
s2.data('Apsara',21)
print(s1.name)
print(s1.age)
print(s2.name)
print(s2.age)

class Student:
    def __init__(self, name, age):  # Fixed __init__
        self.name = name
        self.age = age

s1 = Student('Apsara', 21)
print(s1.name)
print(s1.age)

#dunder methods,operator overloading\
class Point:
    def __init__(self, x):
        self.x = x
    def __add__(self, other):
        return Point(self.x + other.x)
p1 = Point(3)
p2 = Point(4)
p3 = p1 + p2
print(p3.x)

#inheritance
class Animal:
    def speak(self):
        print('Animal sound')

class Dog(Animal):
    def bark(self):
     print('Bark')

d=Dog()
print(d.speak())
print(d.bark())

class Animal:
    def speak(self):
        print('Animal sound')

class Dog(Animal):
    def speak(self):
     print('Bark')
d=Dog()
print(d.speak())

#factory and singleton
class User:
    def __init__(self,role):
        self.role=role
def create_user(role):
    return User(role)
u=create_user('admin')
print(u.role)

class Singleton:
    _instance=None
    
    def __new__(cls):
        if cls._instance is None:
            cls.instance =super().__new__(cls)
        return cls._instance
a= Singleton()
b=Singleton()
c=Singleton()
print(b is c)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner          
        self.balance = balance      

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  # Add money
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount  # Subtract money
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds!")
        else:
            print("Withdraw amount must be positive!")

    def get_balance(self):
        return self.balance
    
account = BankAccount("Alice", 100)
    # account.deposit(50)  
    # account.withdraw(70)  
print("Current balance:", account.get_balance())
    
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner          
        self.balance = balance      

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  # Add money
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount  # Subtract money
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds!")
        else:
            print("Withdraw amount must be positive!")

    def get_balance(self):
        return self.balance
    
account = BankAccount("Alice", 100)
print( account.deposit(50) ) 
print(account.withdraw(70)  )
print("Current balance:", account.get_balance())

