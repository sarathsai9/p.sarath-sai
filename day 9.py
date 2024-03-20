#Day-9

#1.) Write a Python script to generate and print a dictionary that
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings
'''
s1 = "Hello how are you"
s2 = "Hello how is"
s1 = s1.split(" ")
s2 = s2.split(" ")

for val in s1:
    if val not in s2:
        print(val)
       
for val in s2:
    if val not in s1:
        print(val)
       
 '''      




# 3.)Wrire a code print the 8th fibanochi number
#0,1,1,2,3,,5,8

#n1 = 0
#n2 = 1
#ans = 0+1==>1

#n1 = 1
#n2 = 1
#ans = 1+1==>2

#n1 = 1
#n2 = 2
#ans = 1+2==>3

#n1 = 2
#n2 = 3
#ans = 2+3==>5

# find the 8th fibnochi number

#num = 5
#n1 = 0
#n2 = 1
#for val in range(num):
 #   ans = n1+n2
  #  n1 = n2
   # n2 = ans
    #print(ans)


#Constructors
#Eg:2

# unparametarised constructor
'''
class profile:
    def __init__(self):
       print("Hello world")

obj = profile()
obj.__init__()

'''
'''
#Eg:3
#parametarised constructor
class profile:
    def __init__(self, id, name,age):
        print(id, name, age)

obj = profile(1, "chandu",19)
'''
#Eg:4
#class c1:
   # name = "sid"
    #place = "cbe"

 #   def m1(self):
  #      print(self.name, self.place)

#object = c1()
#object.m1()

'''
#Eg:5
class c1:
    def m1(self):
        name = "chandu"
        age = 19
        return name, age
    def display(self):
        #print(name,age)
        #print(self.name,self.age)
        print(self.m1())

object = c1()
object.display()
'''
'''

#? Eg:6
# to use the variables inside the constructor in another methods
class class1:
    def __init__(self):
        self.name = "chandu"
        self.email = "chandu@gmail.com"
        #return name, email #error---> cannot use return with constructor

    def display(self):
        print(self.name, self.email)

c1 = class1()
c1.display()
'''

#--------->Inheritance
# The process of utilizing the methods and attributes of parent class
# throught the objects of child class it is called as inheritance

'''
# 5 types of Inheritance
single  Inheritance
multilevel Inheritance
multiple Inheritance
Hybrid Inheritance
Heirarichal Inheritance
'''

#Single Inheritance
# It has only one parent class and only one child class

'''
#Eg:1
class parent:
    def m1(self):
        print("I am parent class")

class child(parent):
    def m2(self):
        print("Iam child class")

obj = child()
obj.m1()
'''

#Eg:2
#class c1:
#    def __init__(self):
#        print("I am constructor from parent class")

#class child1(c1):
#    pass

#obj = child1()

# ! Eg:3
'''
class parent:
    name = "chandu"

class child(parent):
    name = "name1"

    def display(self):
        print(self.name)

d = child()
d.display()
'''
# ! multilevel inheritance
# ? Eg:1
'''
class voice:
    def sound(self):
        print("all the animals have their own voices")

class dog(voice):
    def dog_voice(self):
        print("meow")

class cat(dog):
    def cat_voice(self):
        print("bark")

class parrot(cat):
    def parrot_voice(self):
        print("speak")

all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()
'''
'''
# ? Eg:2
class honda_city:
    def engine_specs(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, njum_of_piston)

    def honda_city_body_specs(self, color, weight, height, length, vehical_type):
        print(self, color, weight, height, length, vehical_type
             
class amaze(honda_city):
    def amaze_engine_specs(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, num_of_piston)

class civic(amaze):
    def civic_engine_spece(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, num_of_piston)
 
    def civic_body_spece(self, color, weight, height, length, vehical_type):
        print(self, color, weight, height, length, vehical_type)

class amaze(Honda_city):
     def amaze_engine_spece(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, num_of_piston)
 
    def amaze_body_spece(self, color, weight, height, length, vehical_type):
        print(self, color, weight, height, length, vehical_type)
'''
'''
# Multiple Inheritance
 #? It has multiple parent and 1 child
class while_pertol:
    def function_w(self):
        print("used to Airplans")

class Organic_petrol:
    def function_o(self):
        print("used for Bike, cars")
class premium_petrol:
    def function_p(self):
        print("spots cars, bikes")
class petrol(while_pertol, Organic_petrol, premium_petrol):
    def defanition(self):
        print("Petrols types")
p=petrol()
p.defanition()
p.function_o()

# Eg:2
# MRO---> Method resolution Order
class addition:
    def add(self, a, b):
        print(a+b)
    def mul(self,a,b):
        print(a%b)
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)

       
calc=division()
calc.add(3,4)
calc.mul(4,2)
'''
'''
# ! Heirarical inheritance
#? The one parent classe will asct as parent for all the child classes
class catagory:
def weight(self, weight): print(weight)
I
def display(self, color, taste): print(color, taste)
class Tomato(catagory):
def tomato_specs (self):
color="black"
taste "neutral taste"
self.display(color, taste)
class carrot (catagory):
def carrot_specs (self):
    color="green"
   
'''

'''
#Hybrid Inheritance
# The combination of above 4 inheritance is called Hybrid inheritance
class c1:
    def m1(self):
        print("Class1")
class c2:
    def m2(self):
        print("class2")
       
class c3(c2):
    def m3(self):
        print("Class 3")
       
class c4(c3):
    def m4(self):
        print("Class 4")
       
    def m3(self):
        print("iam m3 from c4")
class c5(c4):
    def m5(self):
        print("Class 4")
       
class c6(c5, c3):
    def m6(self):
        print("Class 4")
obj = c6()
obj.m3()
'''

# ! -----------> polymorphism
# poly - many, morph --> form
# a function which has the ability to perform more 1 functionality
# then it is considered to be as polymorphism

# * polymorphism in builtin functions
# len() --> which is used to find the length of list, tuple, dict etc..
# index()
# max()
# min()
# count()
# pop()
# and more...

# * polymorphism in operators
# +
# print(8+8)
# print("k"+'1')
# print([1,2,3][5,6])

# *
print(6*7)
l1 = {12,3,4,5,6}
print(*l1)
#def f1(*args)
l1 = [1,2,3,4]
print(l1*10)

# polymorphism in clsses
# we can achieve polymprphism in 2 ways
# 1.) method overloading --> it is not possible in python
# 2.) method overloading

#) tasks
# write the code for the below tasks using function
# 1.) d1 = {"shift": 1000, "pant": 1500, "shoes": "900", handkey": 30}
# a.) find the min ans max priced prodect
# b.) find the prodect starts with 's' and 's'

# 2.) find the n = 67, is strong number or not

# 3.) l1 = [1,2,3,4,5,6]
# n=2 --> [5,6, 1,2,3,4]
# n=3 --> [4,5,6 1,2,3]
