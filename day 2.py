# a, b = 7, 8
# print(a, b
# print(type(a))


# a, b, c = 9, 8, 7, 8,
# print(a, b, c)

#a, b=c=7, 8
# print(a)
# print(b)
# print(c)

# a=b, c = 4, 2
# print(a, b, c)

# ----> swapping of variables
# a = 7
# b = 5
# temp = a
# a=b
# b=temp
# print(a,b)

# temp = is used to replaced the a,b values

# Eg:2
# a= a+b  #a=12
# a= a-b  #b=12-5=7
# c= a-b  #a=12-7=5

# print(a,b)

# a, b=b, a # only in python
# print(a,b)

# a=a*b  #a=35
# b=a/b  #b=35/7=5
# a=a/b  #a=35/5=7
# print(int(a), int(b))

  # id function: id ()--> it is usedto find memory address of the variable
  

# a = 7
# b = 8
# print(a)
# print(id(a))
# print(id(b))


  #----> keywords#
# keywords are reserved word which provides special meaning to
# compiler or interpretor

# to check if the strimg is keyword or not
# print(keyword.is keyword("sid"))# false

  #if =8
# print(if)# error coz if is akeyword

# !----> literals
# literals is the constant value assaigned to a variable
# a variable is considers to be constant when it is defines
# on caps

# a= 78 # a is variable
# A= 78 # A is constat

# hash() --> it creates a hash value for constant datatype and
# provides srror for non constant datatypes
#n1 = 87+7j
#print(hash(n1))

#f1 = [7, 8, 9]
#print(hash(f1))# error --> list is non-constant or multiple data

# a=9
# b=9
# print(id(a))
# print(id(b))

# Here the id were stored in the same location

# a=9
# b=8
# print(id(a))
# print(id(b))

# ! ----> operators
# ? operators are symbols which is used to perfeorm various opearions
# ? between 2 or more operands


# arithmatic
# assignment
# logical
# relational or comparison
# bitwise
# identity
# membership

# todo ----> arithmatic -->+, -, *,?,%,//, **
# Eg:1
# a = 8
# b = 6
# c = 9
# print(a+b+c)

# input() --> used to get the runtime input
# eval() --> used to get the runtime values of all datatype

# n1 = eval(input("Enter the value:"))
# print(type(n1))

a = 4
b = 2
# print(a/b) # is used to get the quotient value
# print(a%b) # is used to get the remainder value

# ! // --> flpoor desivion

# a = 765433
# b = 19
# print(a/b) # -> the output will be in integer & the output will be
# based on floor value

# ! ** --> used for power of a number
# print(2**4) # --> 16

# ! assignment --> +-=, -=, /=, *=, //=, **=, &=, |=, %=
# a= 8
# a++2 print(a)

# a=30
# b= 7
# print (a)

# ! compaariosn --> ==, >,<, !=, >=
# a = 8
# b = 7
# print(a>B) # true

# a = 9
# b = 5
# print (a==b)

# ! bitwise operator --> &, |, ^, ~, <<, >>
#a = 7
#b = 4
#print(a&b)

# AND
# A B A&B



# 2^4 2^3 2^2 2^1 2^0
# 8    4    2    1

# 0    1    1    1    # --> 7
# 0    1    0    0    # --> 4 &
# -----------------------
# 0     1    1    1 # --> 7

# ~ --->
# a = 9876
# print(~a)


# a = 9

# 128 64 32 16 8 4 2 1
#  0   0  0  0 1 0 0 1 # -->  9

#  1    1  1  1 0  1 1 0 # --> -10

# 0 0 0 0 1 0 1 0 --> 10

# 1 1 1 1 0 1 -> 1s compliment of 10
          # 1 -> 2s compliment
# ----------------------
# 1 1 1 1 0 1 1 0  --> -10

# 256 128 64 32 16 8 4 2 1
#  0   0   0  0  0 0 1 0 1  3<
#  0   0   0  1  0 1 0 0 0 --> 40
# 107

# <<,>>
# print(5>>1)
# 16>4


# ! logical --> used to compare the expressions
# and, or , not
#a = 6
# print(a>3 and a<10)
# print(a>7 or a<30)
# print(not(a>8 and a<10))

#! identify operator
# is, is not
# a = 8
# b = 8
# print(a is b)
# print(a==b)

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a is not b)

# ! membership operator
# in not in

# l1 = [7, 8, 9, 0, 6, 5]
# num = 55
# print(num in 11)

# 11 = [7, 8, 9, 0, 6, 5]
# num = 55
# print(num not in 11)

# num = 678
# print(8 in num 0 # error

# ! 14 conditional statement
# if, elif, else

# --> c syntax
# if (cindition){
#    statement;
#    statement;
#    statement;
# }
# python syntax
# if condition;
#    statement;
#    statement;
#    statement;

# Eg:2
# a = 6
# if a >3:
# print("yes")
# else;
# print("no")

# Eg:3
# if 7>8:
#     print("hello")

# print("no")

# eg:4
# a = 0
# a = none
# a = false
# a = ""
# if a:
#      print("yes")
# else:
#      print("no")
# a number is even or odd
n = int (input("enter the number:"))
if n %2==0:
    print(n, "is even")
else:
    print(n, "is odd")
# name, age, nationality
# 18 above, indian

name = input("enter the name:")
age  = int(input("enter the age:"))
nationality =(input("enter the nationality:"))

if age>=18 and nationality=="indian":
    print("eligible for vote")
else:
    print("not eligible")

    





  






    










  
