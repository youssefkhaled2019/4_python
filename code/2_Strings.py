# ======================= Strings =======================
# a = "Hello, World!"
# a*3 

# print(a[1])

# for x in "banana":
#   print(x)

# txt = "The best things in life are free!"
# print("free" in txt)
# print("expensive" not in txt) #True

# a = " Hello, World! "
# a[::-1] #a[ from : to   :step] #step -1 to reverse 
# print(a[:])
# print(a[2:5])
# print(a[-5:-2])
# print(a.upper()) 
# print(a.lower()) 
# print(a.count('z'))   
# print(a.strip()) # returns "Hello, World!" 
# print(a.replace("H", "J"))
# print(a.split(",")) # returns ['Hello', ' World!'] 
# print(sorted(list(a)) ) #print(sorted(a) )       #[' ', ' ', ' ', '!', ',', 'H', 'W', 'd', 'e', 'l', 'l', 'l', 'o', 'o', 'r']
# print(set(a) ) #{' ', '!', 'd', 'e', 'l', 'o', 'H', 'r', ',', 'W'}

# =======================  =======================

# x = "12354785669854412503665" 
# x.split("5",maxsplit=6) ['123', '478', '6698', '4412', '0366', '']

# x = "12354785669854412503665\nddfdfdfdfdf\nddddddd" 
# x.splitlines()                                          #['12354785669854412503665', 'ddfdfdfdfdf', 'ddddddd']

# a = "yousefrkhaled20147@gmail.com-ahmed@fkrhaled20147 " #split text 3 parts from left
# a.partition('@') #('yousefrkhaled20147', '@', 'gmail.com-ahmed@fkrhaled20147 ')
# a = "yousefrkhaled20147@gmail.com-ahmed@fkrhaled20147 " #split text 3 parts from right
# a.rpartition('@') #('yousefrkhaled20147@gmail.com-ahmed', '@', 'fkrhaled20147 ')

# a.find('@')# position 18  if not found return -1
# a.rfind('@')#position 34

# a.index('@')#18  if not found  ==  error
# # a.rindex('@')#34

# try:
#     a.index('@')
# except:
#     print(" not found ")  



# a.capitalize() 
# a.title() 
# a.upper() 
# "yousefrkhaled".center(30) #'        yousefrkhaled         '
# "YOUsefrkhalED".swapcase() #'        youSEFRKHALed         ' # change captel to small and change small to captel
# "yousefrkhaled".ljust(30) #'yousefrkhaled                 '
# "yousefrkhaled".rjust(30) #''                 yousefrkhaled'
# "yousefrkhaled".rjust(30,'-') #'-----------------yousefrkhaled'
# '435'.zfill(10) #0000000435
# " yousefrkhaled ".strip()#'yousefrkhaled'
# " yousefrkhaled ".rstrip()#' yousefrkhaled'
# " yousefrkhaled ".lstrip()#'yousefrkhaled '
# "**abc**".strip("*")#'abc' # "**abc**".replace("*","")
# "youssef".endswith("f")
# "youssef".startswith("y")
# "-".join(['a','b','c']) #'a-b-c'   # ' '.join('hello')#'h e l l o'

# "ddd".isalpha()
# "142.3".isdecimal()
# "142".isnumeric()
# "232323".isdigit()
# ....more fro is___()

# =======================  =======================
# print(r"sweet \n home alabama" )


# a , b = 'aaaa' , 'bbbbb' 
# print(a,b,end=' ')

# y,yy = 'youssef',1010.33
# x="sweet home %s" %y
# x="sweet home %d" %yy 
# x= "sweet %s %d" % ( y , yy)
# x="sweet home %8d"%yy #sweet home     1010  # add string yy 8 digets and and other space 
# x="sweet home %08d"%yy #sweet home 00001010  # add string yy 8 digets and and other 0 
# x="sweet home %.8f"%yy #sweet home 1010.33000000 


# "{}{}".format("youssef",1222)#'youssef1222'
# '{1} and {0}'.format('red', 'blue')
# "First: {first}. Last: {last}.".format(last='Z', first='A')
# "pi = {0:.3f}".format(3.12528445)
# '{:s} {:d} years old'.format('Im',20)
# '|' + '{:^51}'.format('Hello') + '|'  # ==>  '|                       Hello                       |'
# '{0:10} ==> {1:10d}'.format('name', 56322) # 'name       ==>      56322'


# age = 36
# price = 59.4566 
# txt = "My name is John, I am " + str(age)
# txt = f"My name is John, I am {age}"
# txt = f"The price is {price:.2f} dollars" 
# txt = f"The price is {20 * 59} dollars" #{20 * 59}-> 1180 
# txt ="My name is John, I am %d-%.2f"%(age,price)
# print(txt)


# txt = "We are the so-called \"Vikings\" from the north."
# txt = 'It\'s alright.'
# txt = "This will insert one \\ (backslash)."
# txt = "Hello\nWorld!" 
# txt = "Hello\rWorld!"#Carriage Return
# txt = "Hello\tWorld!" #Tab
# txt = "Hello \bWorld!" #Backspace
# # \f  #Form Feed
# txt = "\110\145\154\154\157"#Hello  #octal value
# txt = "\x48\x65\x6c\x6c\x6f"#Hello  #hex value
# print(txt)


# Code 	    Result 	Try it      <---------------       https://www.w3schools.com/python/python_strings_escape.asp
# \' 	    Single Quote 	
# \\ 	    Backslash 	
# \n 	    New Line 	
# \r 	    Carriage Return 	
# \t 	    Tab 	
# \b 	    Backspace 	
# \f 	    Form Feed 	
# \ooo 	    Octal value 	
# \xhh 	    Hex value

# Method 	        Description     <---------------     # https://www.w3schools.com/python/python_strings_methods.asp
# capitalize()	    Converts the first character to upper case
# casefold()	    Converts string into lower case
# center()	        Returns a centered string
# count()	        Returns the number of times a specified value occurs in a string
# encode()	        Returns an encoded version of the string
# endswith()	    Returns true if the string ends with the specified value
# expandtabs()	    Sets the tab size of the string
# find()	        Searches the string for a specified value and returns the position of where it was found
# format()	        Formats specified values in a string
# format_map()	    Formats specified values in a string
# index()	        Searches the string for a specified value and returns the position of where it was found
# isalnum()	        Returns True if all characters in the string are alphanumeric
# isalpha()	        Returns True if all characters in the string are in the alphabet
# isascii()	        Returns True if all characters in the string are ascii characters
# isdecimal()	    Returns True if all characters in the string are decimals
# isdigit()	        Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()     	Returns True if all characters in the string are lower case
# isnumeric()	    Returns True if all characters in the string are numeric
# isprintable()	    Returns True if all characters in the string are printable
# isspace()	        Returns True if all characters in the string are whitespaces
# istitle() 	    Returns True if the string follows the rules of a title
# isupper()	        Returns True if all characters in the string are upper case
# join()	        Joins the elements of an iterable to the end of the string
# ljust()	        Returns a left justified version of the string
# lower()	        Converts a string into lower case
# lstrip()	        Returns a left trim version of the string
# maketrans()	    Returns a translation table to be used in translations
# partition()	    Returns a tuple where the string is parted into three parts
# replace()	        Returns a string where a specified value is replaced with a specified value
# rfind()	        Searches the string for a specified value and returns the last position of where it was found
# rindex()      	Searches the string for a specified value and returns the last position of where it was found
# rjust()	        Returns a right justified version of the string
# rpartition()	    Returns a tuple where the string is parted into three parts
# rsplit()	        Splits the string at the specified separator, and returns a list
# rstrip()	        Returns a right trim version of the string
# split()	        Splits the string at the specified separator, and returns a list
# splitlines()	    Splits the string at line breaks and returns a list
# startswith()	    Returns true if the string starts with the specified value
# strip()	        Returns a trimmed version of the string
# swapcase()	    Swaps cases, lower case becomes upper case and vice versa
# title()	        Converts the first character of each word to upper case
# translate()   	Returns a translated string
# upper()	        Converts a string into upper case
# zfill()	        Fills the string with a specified number of 0 values at the beginning
