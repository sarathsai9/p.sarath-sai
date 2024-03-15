# ! ------> common functions for list

#l1 = [6, 7, 8, 9, 10]
#print(len(l1))

#print(max(l1))
#print(min(l1)


#l1 = [6, 7, 8, 9, "p", "u"]
#print(max(l1)) --> error coz its a combination of int and string
#print(min(l1)) --> error coz its a combination of int and string

#l1 = [6,6,6, 7, 8, 9, 0, 8.89, -5, 0.78]
#index() --> to get index value of specific element



#l1 = [6,6,6, 7, 8, 9, 0, 8.89, -5, 0.78]
#count() --> how many num of times an element is repeated
#print(l1.count(6))


#! some functions which is specifically used for list

# To add element inside list
# ? insert(index_value, element)--> to ad element at specific index position
#l1 = [6,6,6, 7, 8, 9, 0, 8.89, -5, 0.78]
#l1.inset(2, "cars")
#print(l1)

# ? To delete element from list
#l1 = [6,6,6, 7, 8, 9, 0, 8.89, -5, 0.78]
#pop() ---> last element will be deleted
#l1.pop()
#print(l1)












#* clear() --> to complete delete all element in list
#l1.clear()
#print(l1)

# del -. to delete the list
#del l1 #or del(l1)
#print(l1)


# ? -----> join 2 lists

#l1 = [9, 0, 8]
#l2 = ["p", "o", "t", 34]
# * print(l1+l2)

# ! or

# extend() --> to combine 2 lists
#l1.extend(l2)
#print(l1)

# ? ----> copy()
#l1 = [6, 7, 8, 9, 3]
#l2 = l1.copy()
#print(l2)
#print(l1)

#print(id(l1))
#print(id(l2))

# ! diff between shallow copy and deep copy
# shallow copy
#import copy
#l1 = [8, 9, 0,[5, 6], [3, 2, 1]]
#l2 = copy.copy(l1)
#l1.append(890)
#print(l1)
#print(l2)


# * deep copy --> used to copt the list with nested list
#import copy
#l1 = [8, 9, 0,[5, 6], [3, 2, 1]]
# print(l1[-1][1]) --> to index nested list

#l2 = copy.deepcopy(l1)
#l1[-1].append('cars')
#print(l1)
#print(l2)

# ? sort --> arrange elements in list in ascending order
#l1 = [9, 7, 45,0,-6, 5, 12]
#l1.sort() # to arrange in ascending order
#print(l1)

#l1.sort(reverse=true)
#print(l1)


#l1 = ['z', 'i', 'o', 'p',9]
#l1.sort()
#print(l1)# --> error

# ? list constructo
# list() --> to conver other collection datatype to list
#l3 = ((8, 9, 0))
#print(list(l3))

#l4 = (8,9)
#print(list(14))

# ! ---> nested list
#l1 = [8,9,[0, 8, 7], ["p", "o", "y"], [8, 't']]
#print(l1[-2][1]) # --> o

#print(l1[1:4])
#print(l1[1:-1])

# ? to delete "t" from l1
#l1[-1].remove('t')
#print(l1)


# ? combine these ["p", "o", 'y'], [8, 't'] lists in l1 to ["p", "o", 'y', 8, 'T']

#l1 = ["p","o",'y']
#l2 = [8,'t']
#print(l1+l2)

# ! -------> yuple
# char of tuple

# 1.) tuple have to be surrounded by 9)
# 2.) the elements inside tuple are not changable
# 3.) the element inside tuple are indexed
# 4.) the element will execute in order
# 5.) it is heterogenous
# 6.) it allow duplicate elements

# Eg:
#t1 = (8, 8, 9, 6, 5.78, [9, 0], (6, 8), "moye moye", 9+6j)
#print(t1)
#print(type(t1))

# ?indexing, slicing are all same as list

#l1 = (8)
#print(type(l1)) #int 

#l1 = (8,)
#print(type(l1)) #tuple

#t1 = 8,9
#print(type(t1)) 
   
#t2 = 9,
#print(type(t2))

#len(), min(),max(), index(),count() --> all same as list

# to add element inside tuple --> cannot add
# cannot delete any element from tuple

# join 2 tuples
#t1 = (8, 9, 0)
#t2 = (6, 7, 8)
#print(t1+t2)

# to add all element inside list and tuple

#sum()
#l1 = (8, 9, 7, 6)
#print(sum(l1))

# sort tuple
#t1 = (8, 9, 0, 89,12)
#print(tuple(sorted(t1)))
#print(tuple(sorted(t1,reverse=true)))

# iterate list and tuples

#l1 = [9,8,0,6,5]
#for i in l1:
#print(i)    

# iterate based on elements
#l1 = [9,8,0,6,5,8,56]
#for i in range (0, len(l1)):
#print(l1[i])                

# ! ----> strings
#s1 = 'o'
#print(type(s1))

#s1 = "u"
#print(type(s1))

#s1 = "hello world"
#to acces string
#print(s1)
#indexing and slicing --> same as list and tuple
#print(s1[0:5])

# ---> common functions

# lrn(), min(), max(), index(), count()
#s1 = "hello world"
#print(len(s1))
#print(max(s1))
#print(min(s1))

#ord() ---> used to find the ASCII value of a character
#s1 = 'u'
#print(ord(s1))


# funtions of string
#s1 = "hello world"

# ? to convert all characters to upper case
#print(s1.upper())

# ? to convert to lower case
#s1 = "senior junior"
#print(s1.lower())

# ? strip() --> to eliminate the space in beginning and end of string''
#s1 = "your wellwisher"
#print(s1.lstrip())

# ? split() --> to split the words in srting based on a character
#s1 = "you are the mine"
#print(s1.split('y'))
#print(s1.split('m'))
#print(s1.count('r'))

# replace() --> to replace a specific char in the string
#s1 = "jai sree ram"
#print(s1.replace('e','&&'))

# swapcase() --> to convert capital to saml to capital at a time
#s1 = "hello boys"
#print(s1.swapcase())

# title() --> to write the string in formate of title
#s1 = "dont expect anything"
#print(s1.title())

# capitalize() --> 1st char of string will be converted to capital
#s1 = "bullsheet guy"
#print(s1.capitalize())

# join the strings
#s1 = "hello"
#s2 = "madam"
#print(s1+s2)

#s1 = '''where are you
#iam in kadapa
#and you
#'''
#print(s1.splitlines())

#* find() --> to find the index based on a character
#s1 = "hello namaste"
#print(s1.find('h'))
#print(s1.index('a'))

#* join() -->
#l1 = ["hey","prabu"]
#print(" ".join(l1))
#print("$".join(l1))

#s1 = "welcome to all"
#print(s1.endswith('1'))
#print(s1.startswith('w'))

#s1 = "67"
#print(type(s1))
#print(s1.isdigit())

#* print the strind in reverse manner
#s1 = "pattan"
#print(s1[::-1])

# ! ---> Eg:1
# wap to find the number of lower case letters
#s1 = "I MISS you"
#count = 0
#for i in s1:
#    if i.islower():
#        count+=1
#print("the total num of lower case letters: ",count)        


# ! -----> Eg:2 r---> "$"
#s1 = 'restarter'
#fst = s1[0]
#bal = s1[1:]
#3txt = bal.replace(fst,"$")
#print(fst+txt)

# ! ------> Eg:3

s1 = '''
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also the leap into electronic typesetting,
remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
and more recently with desktop publishing software
like Aldus PageMaker including versions of Lorem Ipsum.'''

s1 = s1.strip()
characters = len(s1)
print(characters)

words = s1.split(" ")
print(len(words))

sentenses = s1.split('.')
for val in sentenses:
    if val =='':
        index = sentenses.index('')
        sentenses.pop(index)
print(len((sentenses)))

space = 0
for val in s1:
    if val ==" ":
        space=space+1
print(space)        
      
































    


      
