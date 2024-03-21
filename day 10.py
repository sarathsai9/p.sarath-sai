# day 10

#! -----> tasks
# write the code for the below tasks using function
# 1.) d1 = {"shift": 1000, "pant": 1500, "shoes": "900", handkey": 30}
# a.) find the min ans max priced prodect
# b.) find the prodect starts with 's' and 's'

# 2.) find the n = 67, is strong number or not

# 3.) l1 = [1,2,3,4,5,6]
# n=2 --> [5,6, 1,2,3,4]
# n=3 --> [4,5,6 1,2,3]

# ! method riding
# * polymorphism in classes
'''
class bank:
    def ratio(self):
        print("ALL banks has repo rate")

class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")

class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")

i = IOB()
i.ratio()

s = SBI()
s.ratio()
'''

# ? Eg:2
'''
class USA:
    def langauge(self):
        print("english")

    def capital(self):
        print("washington DC")

class india(USA):
    def langauge(self):
        print("none")

    def capital(self):
        print("new delhi")

I = india()
I.langauge()
I.capital()
'''

# Eg:3
# polymorphism using objects

# c1, c2 --> c1 = print(c1), print(c2)
# f1, f2
'''
class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
        super().f1()
        print("class 2")

obj1 = c2()
obj1.f1()
'''
# * Eg:4
'''
class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
        print("class 2")

obj1 = c2()
obj2 = c1()

def display(a):
    a.f1()
display(obj1)
display(obj2)
'''
# * changing the funtionality of builtin functions
'''
class shoping:
    def __init__(self, l1):
        self.items = l1

    def __len__(self):
        length = len(self.items)
        return length
s = shoping([1,2,3,4,5,6,7,8,9])
print(len(s))
'''
'''
# ! --> method overloading
# ! Eg:1
class suming:
    def add(self, a, b):
        print(a+b)

    def add(self, a, b, c):
        print(a+b+c)

s = suming()
#s.add(4,3)# ------> error
s.add(4, 5, 1)
'''
'''
#Eg:2
class summing:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!= None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print(a)
obj=summing()
obj.add(2)
obj.add(3,4)
obj.add(1,2,3)
'''
# ! ------> abstraction
# the process of hiding the implimnetation details is abstraction
'''
# ? Eg:1
from abc import ABC,abstractmethod
class shapes(ABC):
    @abstractmethod
    def sides(self):
        print("All shapes have sides except circle")

class triangle(shapes):
    def triangle_sides(self):
        print("3 sides")

class square(shapes):
    def square(self):
        print("4 sides")

tr = triangle()
tr.triangle_sides()

# To write the capital letters

def decor(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner()

@decor
def greet():
    return 'good morning'
print(greet)
'''

#Rules to define abstract class1
#1.) Abstarct class cannot  be instantained
#2.) From abc import ABC, abstractmethod
#3.) subclass the normal class with ABC
#4.) Convert the normal method inside the abstract class to abstract method
#5.) All the child classes have to be subclassed with abstract class
#6.) The abstract method should be present in the child classes


#Eg:2
'''
#
from abc import ABC,abstractmethod
class c1(ABC):
    @abstractmethod
    def m1(self):
         print("This is abstract class")

   
class c2(c1):
    def m2(self):
        super().m1()
        print("I am child")

    def m1(self):
        pass

class2 = c2()
class2.m2()

'''
'''
#Eg:3
from abc import ABC,abstractmethod
class password(ABC):
    @abstractmethod
    def pswd(self):
        pswd- "SAI2003"
        return pswd

class login(password):
    def validate(self, name, password):
        if super().pwd() ==password:
            print("welcome",name,'!!')
            print("Login succesfull")
        else:
            print("please check the password")

    def pwd(self):
        pass

login = login()
name = input("Enter the name: ")
pwd = input("Enter the password: ")
login.validate(name,pwd)
    
'''


# Encapsilation
#Eg:1
'''
class car:
    name = "BMW" # private variable
    print(__name)

c1 = car()
print(c1.name)# error
c1.name = "Audi"
print(c1.name)#error
'''

#Eg:2
# Accessing private data outside the class
'''
class c1:
    __phone = "9390982720"

    def display(self):
        print(self.__phone)
        

c= c1()
c.display()
#print(c.phone)

'''
'''
#Eg:3
# declare private method
class class1:
    def __m1(self):
        print("Iam private method")

c=class1
c.__m1()
'''
'''
# Nested class
class class1:
    class class2:
        name = "sai"

        def display(self):
            print(self.name)

    obj = class1
    obj.obj1.display()
'''

#1.) Write the code for the below tasks using function
#     d1 = {"shirt":1000, "pant":1500, "Shoes":900, "handkey":30}

d1 = {"shirt":1000, "pant":1500, "Shoes":900, "handkey":30}
for val in d1:
    if d1[val] == min(d1.values()):
        print(val)
for val in d1:
    if d1[val] == max(d1.values()):
        print(val)
for val in d1:
    if val.startswith('s') or val.startswith('S'):
        print(val)


























































        

