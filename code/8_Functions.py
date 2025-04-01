def info():
    pass
print(info())#return none

#===================function=========================

def star(): 
 a=1
 b=2
 return a,b
x,z=star()
print(x,z) 






#===================function=========================
def my_function(fname, lname):
  print(fname + " " + lname)

def my_function2(*kids):
  print("The youngest child is " + kids[1])

def my_function3(child3, child2, child1):
  print("The youngest child is " + child3)

def my_function4(**kid):
  print("His last name is " + kid["lname"])  

def my_function5(country = "Norway"):
  print("I am from " + country)

def my_function6(food):
  for x in food:
    print(x)  

def myfunction11():
  pass


"""
You can specify that a function can have [ONLY positional arguments], or [ONLY keyword arguments.]

To specify that a function can have only positional arguments, add (, / )after the arguments:
To specify that a function can have only keyword arguments, add (*,) before the arguments:

"""


#ONLY positional arguments, or ONLY keyword arguments.
def my_function7(x, /):
  print(x)
def my_function8(x):
  print(x)

#only keyword arguments,
def my_function9(*, x):
  print(x)

def my_function10(a, b, /, *, c, d):
  print(a + b + c + d)

# Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
# =====================

var2 = (1,2,3) 
my_function2(*var2) 
my_function2("Emil", "Refsnes") 

var1 = {'child1':"1",'child2':"2"} 
my_function3(**var1) 
my_function3(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 
my_function4(fname = "Tobias", lname = "Refsnes") 

my_function5("India")
my_function5()

fruits = ["apple", "banana", "cherry"]
my_function6(fruits)

my_function7(5)
# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
my_function8(x = 3) 
# only keyword arguments,
my_function9(x = 3) 
# Combine Positional-Only and Keyword-Only
my_function10(5, 6, c = 7, d = 8) 


tri_recursion(6)



def powers(m,n) :  
    print (m**(n)) 
 
powers(n=3 ,m= 4)

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue') : 
    print ( "-- This parrot wouldn't", action) 
    print ("if you put", voltage, "volts through it.") 
    print ("-- Lovely plumage, the", type) 
    print ("-- It's", state, "!") 
parrot(1000,) # 1 positional argument 
print("-"*40,"\n")
parrot(voltage=1000) # 1 keyword argument 
print("-"*40,"\n")
parrot(voltage=1000000, action='VOOOOOM') # 2 keyword arguments 



#error funtion
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue') :  
    print ( "-- This parrot wouldn't", action) 
    print ("if you put", voltage, "volts through it.") 
    print ("-- Lovely plumage, the", type) 
    print ("-- It's", state, "!") 
 
parrot() # required argument missing 
# parrot(voltage=5.0, 'dead') # non-keyword argument after a keyword argument 
parrot(110, voltage=220) # duplicate value for the same argument 
parrot(actor='John Cleese') # unknown keyword argument 









# ================================================
#                  recursive functions 
# ================================================



def fac(n): 
    if n ==1 :  
        return 1 
    else :  
        return n * fac(n-1) 
 
print(fac(10))

# ================================================
#                  Function 
# ================================================

xx = 5 
def gg() :  
    global xx 
    xx = 14 
gg() 
print (xx)


# Function Inside Function
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

# Nonlocal Keyword
  # -The nonlocal keyword is used to work with variables inside nested functions.
  # -The nonlocal keyword makes the variable belong to the outer function.
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1()) 