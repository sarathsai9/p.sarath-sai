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



















































































        

