class car :  
    length = 15 
    width = 8 
    height = 6 
    color = 'white' 
    volume = length * width * height 
     
print(car.color)


#-----------------------------------
class Person: 
    G='X' #gloabal
    def __init__(self, name,mobile_phone=None, office_phone=None,private_phone=None, email=None): 
        self.name = name 
        self.mobile = mobile_phone 
        self.office = office_phone 
        self.private = private_phone 
        self.email = email 
    def add_mobile_phone(self, number): 
        self.mobile = number 
    def add_office_phone(self, number): 
        self.office = number 
    def add_private_phone(self, number): 
        self.private = number 
    def add_email(self, address): 
        self.email = address 
    def dump(self): 
        s = self.name + '\n' 
        if self.mobile is not None: 
            s += 'mobile phone: %s\n' % self.mobile 
        if self.office is not None: 
            s += 'office phone: %s\n' % self.office 
        if self.private is not None: 
            s += 'private phone: %s\n' % self.private 
        if self.email is not None: 
            s += 'email address: %s\n' % self.email 
        print (s) 
p1 = Person('Hans Hanson',office_phone='767828283', email='h@hanshanson.com') 
p2 = Person('Ole Olsen', office_phone='767828292') 
p2.add_email('olsen@somemail.net') 
phone_book = [p1, p2] 
for person in phone_book: 
    person.dump() 



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