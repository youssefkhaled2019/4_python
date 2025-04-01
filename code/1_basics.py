# import sys
# print(sys.version)
# >>> python python.py

# import platform
# x = platform.system()
# x = dir(platform)
# print(x) 
# =====================[Variables]=========================
# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0 
# c = complex(x)   #c.real ,c.imag 
# bool("Hello")
# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex #3+5j
# x = 35e3   # <class 'float'>
# y = 12E4   # <class 'float'>
# x, y, z = "Orange", "Banana", "Cherry"
# x = y = z = "Orange"
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
#  ************************************
# x = "awesome"
# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)
#   myfunc()
# print("Python is " + x) 

# x = "awesome"
# def myfunc():
#   global x
#   x = "fantastic"
# myfunc()
# print("Python is " + x) 


# def myfunc():
#   global x                                #To create a global variable inside a function, you can use the global keyword.
#   x = "fantastic"
# myfunc()
# print("Python is " + x)#Python is fantastic
# =====================[Data Types]=========================
# Text Type: 	    str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	    set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview
# None Type: 	    NoneType




# x = range(6) #range
# x = b"Hello" 	#bytes
# x = bytearray(5) 	#bytearray                              #??
# x = memoryview(bytes(5)) 	#memoryview
# x = None 	#NoneType
# x = ["apple", "banana", "cherry"]    list
# x = ("apple", "banana", "cherry") 	tuple
# x = {"name" : "John", "age" : 36} 	dict
# x = {"apple", "banana", "cherry"} 	set
# x = frozenset({"apple", "banana", "cherry"}) 	frozenset   #??
#  ************************************
# x = str("Hello World") 	str
# x = complex(1j) 	complex
# x = list(("apple", "banana", "cherry"))
# x = tuple(("apple", "banana", "cherry"))
# x = dict(name="John", age=36)
# x = set(("apple", "banana", "cherry"))
# x = bool(5)
# x = frozenset({"apple", "banana", "cherry"}) 	frozenset
# x = bytearray(5) 	                            bytearray
# x = memoryview(bytes(5)) 	                    memoryview
# x = None 	                                    NoneType
# x = bytes(5) 	#bytes
# x = bool(5) 	bool
# ////////////////////////////////////////////

# =====================[public function]=========================

# #dir(m) for show all premter and verible  import math as m 
# sorted
# list(reversed([1,23]))
# del #delete
# chr(10) #\n
# bin(3) #0b11
# oct(8)#001000 => [001][000]
# ord('a')#97
# abs(-20)  #20
# divmod(102,2) #(51, 0)
# pow(2,3) #8
# min(5, 10, 25)
# max(5, 10, 25)
# round(1.25) #1
# =====================[random]=========================
# import random
# print(random.random()) #between 0-1 size one element float
# print(random.randint(1,20)) #between a-1b size one element int
# print(random.uniform(1,20))#between a-1b size one element float

# print(random.randrange(10)) 
# print(random.randrange(1, 10))  #randrange(start, stop=None, step=1) size one element  int  EX: randrange(0,20,2) retutn even
# print(random.randrange(0,20,2))

# print(random.choice(['a','b','c']))#choice('sweet home alabama')# get one elment
 
# print(random.sample(range(200) ,10))#print 10 utem reandon integer

# items = [1,2,3,4,5,6]
# random.shuffle(items)#Shuffle list x in place, and return None.
# print(items)#[3, 6, 1, 5, 4, 2]
# =======================[bool]=======================
# print(bool(False)) #False
# print(bool(None))#False
# print(bool(0))#False
# print(bool(""))#False
# print(bool(()))#False
# print(bool([]))#False
# print(bool({}))#False

# class myclass():
#   def __len__(self):
#     return 0
# myobj = myclass()
# print(bool(myobj))#False


# x = 200
# y="200"
# print(isinstance(x, int))#True    #??
# print(type(x)==int)
# print(isinstance(y, int))#False
# ======================[if-else]========================

# a = 200
# b = 33
# c = 500

# 15 < a < 30 

# Note  a != b  ,and,or,not,, and == &    ,, or== |            Continue   break  is None ,is not None


# -----------------
x=None
if x is None:
    print("None")
elif x is not None:
    print("not None")
# -----------------

x=5
y=7
if (x==2) & (y==3):#and
    print("None")
elif (x==2) | (y==3):#or
    print("not None")

# -----------------

# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")


# if a > b: print("a is greater than b") 

# print("A") if a > b else print("B") 

# print("A") if a > b else print("=") if a == b else print("B") 

# if a > b and c > a:print("Both conditions are True")

# if a > b or a > c:print("At least one of the conditions is True")

# if not a > b:print("a is NOT greater than b")

# if b > a:pass
# =======================[while]=======================
# i = 1
# while i < 6:
#   print(i)
#   if i == 2:
#     print(i)
#     continue
#   if i == 3:
#     print(i)
#     break
#   i += 1 
# else:
#   print("i is no longer less than 6")  
# ======================[for]========================
# fruits = ["apple", "banana", "cherry"]
# adj = ["red", "big", "tasty"]

# for x in fruits:
#   if x == "banana":
#     break
#   if x == "apple":
#     continue
#   print(x)

# for x in range(6):#range(2, 30, 3)
#   print(x)

# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!") 

# for x in adj:
#   for y in fruits:
#     print(x, y)


#-------------------------------
# print(sum([k for k in range(20)]))
# newlist = [ x**3 for x in range(12)]
#           [3*x for x in [y**2 for y in range(10)]]
# newlist = [x for x in fruits if "a" in x]
# newlist = [x for x in fruits if x != "apple"]   #??
# newlist  = [i for i in range(20) if i%3 ==0  and i %2 ==0 ]
# newlist = [[0 for i in range(5)] for j in range(7)]
# newlist = [x if x != "banana" else "orange" for x in fruits]  #??
# newlist = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
#-------------------------------

# grades  = {"ahmed":35 ,"mona":40 ,"mena":37 }
# for a in grades : print(a)# output -> ahmed  mona mena
# for a in grades.items() : print(a)# output -> ('ahmed', 35) ,('mona', 40),('mena', 37)
# for a,b in grades.items() : 
# for a in grades.keys() : 
# for a in grades.values() : 
#-------------------------------
# for index,val in enumerate(grades,3) : 
#-------------------------------
# students =  ["ahmed","ramy","ramy","mena"]
# grades = [25,33,66,95,444]
# for i,a in zip(students,grades) : 
#  print("student" + i + " got " + str(a) + "degree"  )


# ====================== [try-except] ========================
# IOError , ValueError , ImportError , EOFError , KeyboadInterrupt


# try:
#   print(x)
# except:
#   print("An exception occurred") 


try:
  print(x)
except NameError:
  print("Variable x is not defined")
except ZeroDivisionError as err:
    print("Error message is:", err)  
except:
  print("Something else went wrong")   
finally : 
    print ("end")


# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")  
# finally:                                     #The finally block, if specified, will be executed regardless if the try block raises an error or not.
#   print("The 'try except' is finished")  

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:                                     #The finally block, if specified, will be executed regardless if the try block raises an error or not.
#   print("The 'try except' is finished") 


# x = -1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")  #??  

# try:
#   raise Exception("Sorry, no numbers below zero")  #??  
# except:
#   print("Something went wrong")



# x = "hello"
# if not type(x) is int:
#   raise TypeError("Only integers are allowed") #??  


#  **************** -ex- ********************
# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")  



# ====================== [User Input] ========================
# a,b,c=map(int,input().split(" "))

# ====================modules==========================

# import libraryname 
# import libraryname as ab 
# from libraryname import function 
# from libraryname import * 





# import mymodule
# import mymodule as mx
# from mymodule import person1

# mymodule.greeting("Jonathan")
# a = mymodule.person1["age"]
# print(a) 

# a = mx.person1["age"]

# print (person1["age"])

