# ----> while loop
# -----> break using while loop

# Eg:1
# 1.) iterate from 20 to 30 and break the loop in 27

#i = 20
#while i<31:
#     if i ==27:
#         break
#     print(i)
#     i+=1

# 2.)
#i=20
#while i<31:
#    print(i)
#    if i==27:
#        brak
#    i+=1


# 3.)
#i = 20
#while i<31:
#    print(i)
#    if i==27:
#        break
#    i+=1



# 4.)
#i = 20
#while i<31:
#    if i==27:
#        print(1)
#        break
#    i+=1



# ! -------> continue
# ---> Eg:1
#i = 20
#while i<31:
#    if i==27:
#        continue
#    print(i)
#    i=i+1

#i = 20
#while i<31:
#    i=i+1
#    if i==27:
#        continue
#    print(i)
        

# ! Eg:5
# while to iterate from 12 to 22
# find the sum of all numbers

#i= 12
#sum=0
#while i<23:
#    sum=sum+i
#    i+=1
#print(sum)


# ! Eg:6
# find the average of value from 20 to 25

#i=20
#sum=0
#count = 0
#while i<=30:
#    sum=sum+i
#    count+=1
#    i+=1
#print(sum/count)


# !------> Nested for loop
# Eg:1

#for row in range(8,9):
#    for col in range(2,5):
#        print(row,col)

# Eg:2
# * * * *
# * * * *
# * * * *
# * * * *

#rows = int(input("enter the rows:"))
#cols = int(input("enter the cols:"))

#for row in range(rows):
#    for col in range(cols):
#        print("*",end=" ")
#    print()

#for row in range(6):
#   for col in range(6):
#        print("*", end=" ")
#    print()

#! to prin start in right angled triangle


#for row in range(0,6):
#    for col in range(0, row):
#        print("*", end=" ")
#    print()
    
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

#for row in range(0, 6):
#    for col in range(row,6):
#        print("*",end= "")
#   print()

# Eg:3
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

#for row in range(5):
#    for col in range(5):
#        if col==0 or col==5-1 or row ==0 or row ==5-1:
#            print("*", end=" ")
#        else:
#            print(" ",end=" ")
#
#    print()


# Eg:4
      
#      *
#    * * *
#   * * * *
#  * * * * *

#for row in range(0,5):
#    for col in range(0,6):
#        if (row==0 and col==3) or (row==1) and(col>=2 and col<=4) or(row==2) and (col>=1) and (col<=5):
#            print("*", end=" ")
#        else:
#            print(" ", end=" ")
#    print()

# *
# * *
# *   *
# *     *
# *       *
# * * * * * *

# ----> list

# ! ----> datatypes
# primary

# number --> int, float complex
# string
# boolean
# none

# collection
# list
# tuple
# set
# dictionary

# ? ---> list

# 1.) if the collection of elements are by square brackets, is considered to be list
# ! eg:
    # l1 = [4, 7, 9, 9.89, "hello", 7+9j, [8, 9, 0]]

# charctristicts of list
# 1.) list have to be sorrounded by []
# 2.) it is multable (the elements in the list are changable)
# 3.) every element inside list is indexed
# 4.) the elements inside list will be ordered format
# 5.) it can hold duplicate values
# 6.) its heterogenous

# to access the elements in list
#l1 = [1, 4, 1, 7, 7.5,"p", "i"]
#print(98)

# --> indexing
# in the cillection datatypes like list, tuple, string, the elements will be alloted with pre-pefinded unique value called index value

# we have 2 types of indexing
# positive indexing --> starts with 0 from left hand side
# negative indexing --> starts with -1 from right hand side

# --> positive indexing
# lst1 = [1, 4, 1, 7, 89.7, 7.5, "p" "i"]
# print(lst[0])
# print(lst[4])
# print(lst[20])--> error

# ? ------> negative indexing
# lst = [1, 4, 1, 7,89.7, 7.5, "p", "i"]
# print(lst1[-1])
# print(lst1[-5])

# ? ----> slicing
#lst1 = [1, 4, 1, 7,89.7, 7.5, "p", "i"]
#lst1[start_index:end_index:step]

#print(lst1[0:4])
#print(lst1[6:8])
#print(lst1[3:6])
#print(lst1[:5])
#print(lst1[3:])
#print(lst1[:])

#print(lst1[0:7:1])  # lst1[0:7] --> both are same
#print(lst1[0:7:2])

# trail = int(input())

#lst1 = [1, 4, 1, 7,89.7, 7.5, "p", "i"]
#print(lst1[-4:-1])
#print(lst1[-1:-4]) 
#print(lst1[-7:-1])
#print(lst1[-7:-1:2])

#! to intrest to add element inside list

append() --  used to add element at last position of list
l1 = [9, 8, 0, 6]
11 append("car")
print(l1)










































































    
    
    






































































































































                
