# ===============Class==============================

class Person2:
  pass

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"  
  
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
print(p1)   
print(p1.name)
p1.name="youssef"
print(p1.name)
# ===============Delete=================
# del p1.age 
#  del p1 

print(p1.age)     

print(p1.myfunc())




#=================  Python Inheritance =================
class Student(Person):
  pass  #Note: Use the pass keyword when you do not want to add any other properties or methods to the class.


x = Student("Mike", 20)
x.myfunc()
print(x)

# ********************************
# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

class Student2(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student2("Mike", 2222)
x.myfunc()
# ************** super ******************
# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
class Student3(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student3("Mike", 23345)
x.myfunc()

# ********************************

class Father:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Child (Father):
  def __init__(self, fname, lname,phone=None):
    super().__init__(fname, lname)
    self.years = 2019
    self.phone = phone
  
  def info(self):
    print("Welcome", self.firstname, self.lastname, "to the phone of", self.phone)  


x = Child("Mike", "Olsen")
x2 = Child("Mike", "Olsen",98898888)
# print(x.phone)
# print(x2.phone)
x.info()
x2.info()