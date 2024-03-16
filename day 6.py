# Day : 6
# ! -------->set

# ? characteristics of set
#1.)Set can be created using()
#2.)The elements inside set are not indexed
#3.)Does not allow duplicate values
#4.)It unordered
#5.)Heterogenous -->accept only unmutable datatypes
#6.)Mutable or changable

#Eg:1
#s1 = {9,9,89,7.76,8+7j,(8,7,5),"truck",'e'}
#print(s1)

#Eg:2
#s2 = {5,8,98,[9,0]}
#print(s2)-->ERROR

#Eg:3
#min(),max(),len()

#*Eg
# ? To add element inside set

#s1 = {8,78,67,'u'}
#add
#s1.add(23)
#print(s1)

#update()
#s1.update([9,0])
#print(s1)

# ? To delete element inside set
#s1 = {8,78,67,'u'}

#pop() #to delete one element randonly
#s1.pop()
#print(s1)

#remove()
#s1.remove(78)
#print(s1)

#Dicard()
#s1.discard(8967)
#print(s1)

#clear()
#l1 = {}
#print(type(l1)) #-->Datatype dict

#s1 = set() # to create empty set
#print(type(s1))

#s1 = {8,9,0}
#s1.clear()
#print(s1)

#Del s1
#print(s1)

# * Jointhe sets
#s1 = {9,0,8}
#s2 = {9.90,"sharath",'t',56}
#Union() -->tp combine 2 sets
#s3 = s1.union(s2)
#print(s3)

# * Intersection() -->To get common elements inside set
#s1 = {4,5,6}
#s2 = {5,6,7,8}
#print(s1.intersection(s2))

# *Difference()
#s1 = {4,5,6}
#s2 = {5,6,7,8}
#print(s1.difference(s2))
#print(s2.difference(s1))
#print(s1.symmetric_difference(s2))


# isdisjoint(),issubset(),issuperset()

#s1 = {8,9,0}
#s2 = {6,7,5,9,0}

#print(s1.issubset(s2))
#print(s2.issuperset(s1))

#! --->Problem:1
#s1 = {1,2,3,4,5}
#s2 = {3,2,7,8,9}
#n1 = {1,2,3} 

#for val in s1:
#    if val in s2:
#        str1 = "Its joint set" 
#print(str1)
  

# ! ------> Dictionary
#Eg:1
#d1 = {1:100,'a':200,4.5:"hello"}
#print(d1)
#print(len(d1))


# ? char of dictionary
#1.)Have to surrounded by{}
#2.)It have to be in the form of key ,valuepair
#3.)It is mutable
#4.)Duplicate keys are not allowed,duplicate values allowed
#5.)It is unindexed
#6.)It is ordered
#7.)Key does not allow mutable datatypes,values allow mutable datatype

#d1 = {1:100,2:200,3:300,4:400}
# *To access element in dictionary

#print(d1)
# or
# To access the value ,have to use key
#print(d1[1]) #o/p--->100


# ? some common functions
#len(),min(),max()
#print(min(d1))
#print(max(d1))

# ? To find min,max based on values
#print(min(d1.values()))
#print(max(d1.values()))

# ? Dictionary based functions
#To add element(key and value pair) in dict
#d1 = {1:100,2:200,3:300,4:400}
#d1[5] = 500
#print(d1)


# ? To replace a value in dictionary
#d1 = {1:100,2:200,3:300,4:400}
#d1[2]="tomato"
#print(d1)

# ? Delete element from dictionary
#d1 = {1:100,2:200,3:300,4:400}
#popitem() # --> To delete last key value pair in dict
#d1.popitem()
#print(d1)


#clear(),del

# join 2dictionary
#d1 = {1:100,2:200,3:300,4:400}
#d2 = {"a":"apple","b":"boy","g":"game"}
#d1.update(d2)
#print(d1)

# get() --->used to get the value from a key
#d1 = {1:100,2:200,3:300,4:400}
#print(d1[90])
#print(d1.get(90))

#to print all keys
#print(d1.keys())
#print(type(d1.keys()))

#to print all values
#print(d1.values())


# * Iterate dictionary
#for val in d1:
#    print(val)


# For val in d1.values(): # to Iterate values alone
#for key,val in d1.items():
#    print(key,val)


# ! Problems:1
#n = int(input("enter num of times:"))
#integer =[]
#float_value =[]
#string = []

#for val in range(n):
#    value = eval(input("enter the values:"))
#    if type(val)==int:
#        integer.append(val)
#    elif type(value) ==float:
#        float_value.append(value)
#    elif type(value)==str:
#        string.append(value)
#    else:
#        print("pls provide data in int,float,string")
#print(integer)
#print(float_value)
#print(string)


#! --->Problem:2
# Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}


#set1 = {10, 20, 30, 40, 50}
#set2 = {30, 40, 50, 60, 70}
#set3 = set()
#for val in set1:
#    if val not in set2:
#        set3.add(val)
#for val in set2:
#    if val not in set1:
#        set3.add(val)
#        print(set3)

# ! ------>problem:3
#l1 = [1,2,3,4]#key
#l2 = ["a","b","c","d"]#value
# o/p -->{1:'a',2:'b',3:'c',4:'d'}

#d1 = {}
#for val in range(len(l1)):
#    d1[l1[val]] =l2[val]
#print(d1)




# !or
#c=0
#for val in set1,set2:
#    c=c+1
#    if v==1:
#        for element in val:
 #           if element not in set2:





 


#1.) swap elemwnts in string list
# The original list is :["Ggf", "best", "for", "geeks"]
# List after performing character swaps:]"efg", "is", "bBgst", "for", "eGGks"]
























































































