# day 8

# 1.) Write a Python script to generate and print a dictionary that
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number

#n = int(input("enter a number: "))
#n1=n*n
#print("n:",n1)

# ! Eg:4
#? function with return statement

#1.) A variable can be declared in side the fuv=nction can be outside
#2.) return does not print anything
#3.) we cannot write any code below return statement

#def f1():
#    z = 9
#f1()
#print(z) # error --> cannot use outside the function

#def f1(a, b):
#    c = a*b
#    return c
#print(f1(6,8))
#obj = f1(6, 8)
#obj = f1(4, 6)

#def gracemark(object):
#print(object+4)
#gracemark(obj)
#gracemark(obj1)

#123
# ? problem:
#def palindrome(n):
#    string = str(n)
#    rev = str(n)[::-1]
#    if string==rev:
#        print(n, "palindrome")
#    else:
#        print("not palindrome")
#a = int(input("enter the value:"))
#palindrome(a)
    

# ? based on the declaration of paraneter and args
# ? functio are divided into 5 catadories

# positional args
# keyword args
# default args
# variable length args
# keyword variable length args

#* positional args
#? the position of parameters have to be same as position as arguments
# ! Eg:1
#def profile(name, phone, mark):
#    txt = "my name is {}. my phone number is {}. i got {}marks."
#    print(txt.format(name, phone, mark))

#profile(9390982720, "sharath", 90) # unexpected output


# keyword args
# ! Eg:1
# ? to overcome the dusaadvantage of position args, we use keyword args
# ? it is the process of intialising the parameter with the args while calling the function
#def profile(name, phone, mark):
#    txt = "my name is {}. my phone number is {}. i got {}marks."
#    print(txt.format(name, phone, mark))

#profile(name = "sharru", mark=90, phone=9390982720)


# todo ---> exception of keyword args function
#def profile(name, phone, mark):
#    txt = "my name is {}. my phone number is {}. i got {}marks."
#    print(txt.format(name, phone, mark))

#profile(name = "sharru", 9390982720, mark=90) # error -> position args fiiow keywords
#profile(9390982720, name="sharru", mark=90) # error -> name multiple values
#profile("sharru", mark=90, phone=9390982720)

# * default args
# the method of assigning the to the paremeter while declaring the
# function
# ! Eg:1
#def profile(name, phone, place="kadapa"):
#    if place!="kadapa" or place!="KADAPA" or place=="kadapa":
#        txt = "my name is {}. my phone number is {}. i am from {}."
#        print(txt.format(name, phone, place))
#    else:
#        print("you are not eligible  to sigup")
#profile("sharru",9390982720,)

# exception

#def profile(name, place="kadapa", phone): # error --> coz defult args
                                          # positional param
    
#     if place=="kadapa" or place="KADAPA" or place=="kadapa":
#        txt = "my name is {}. my phone number is {}. i am from {}."
#        print(txt.format(name, phone, place))
#     else:
#        print("you are not eligible  to sigup")
#profile("sharru",9390982720,)

# * variable length params
# ! Eg:1
# to pass more then 1 arg to paremeter means we use variable length args
# to convert normal paremeter to variable length param, add* to ther prefix of param

# name = "sharru", 'amma' 'nanna'3
#def profile(*name):
#    for val in name:
#        print("my name is",val)
#profile("sharru", "amma", "nanna")



# ! Eg:2
#def profile(*name,age):
#    for val in name:
#        print("my name is",val, "may age is ", age)
#profile("sharru", 'name2','name3',28) # error --> age has on args

#def profile(*name,age):
#    for val in name:
#        print("my name is",val, "may age is ", age)
#profile(28, "shrru", 'name2','name3')


# * keyword variable lem=ngth args
# kwaegs --> which is used to provide the args in the form of key value pair.
# ! Eg:1
#def price(**price_list):
#    print(price_list)

#price(shirt=1000, iphone=80000)

#n = 5
#{1:1, 2:4, 3:9, 4:16, 5:25}

#n = int(input("enter the number: "))
#d1 = {}
#for val in range(1, n+1):
#    d1[val] = val**2
#print(d1)
#dict1(5)

# ! ------> object orinted programing
# the paradigms of object oriented programming are

# class
# objects
# inheritance
# polymorphism
# abstraction
# encapsulation

# ! class is a blue print of an object 
#l1 = [1,2,3,4,5,6]

# ? Eg:1
#class c1:
#    name1 = "ss"
#print(name1)

# ? Eg:2
#class person:
#    name = "meow"

#c = person()
# the process of creaction of an object is called as instantion
#print(c.name)

# ? Eg:3
# create of a method
# when the fuction is created with a class is called as method

# ! method without parameter
#class peron:
#    def display(): # it is a method                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
#        print("hello welcom to classes")

#p = person()
#p.display()

#? Eg:4
# ! method without parameter
#class person:
#    def display(person, name, age):
#        print(name, age)

#p = person()
#p.display("ss",98)

# ? Eg:5
#class person1:
#fname = "sharath" #attribute or static variable
#lname = "S"
    
# def first_name(self):
#     print(self.fname)
#     
# def full_name(self):
#     print(self. fname+" "+self.lname)
        
#p = person()
#p.first_name()
#p.full_name
        
# ? Eg:6
# constructors -->__init__()
# this is a special method whcih has ability to execute itself without
# calling it manullay through the process of instantiation

#class profile:
#def __init__(self):
#    print("oye")




















































































