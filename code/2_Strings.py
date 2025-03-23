# =======================Strings ===============
# a = "Hello, World!"
# print(a[1])

# for x in "banana":
#   print(x)

# txt = "The best things in life are free!"
# print("free" in txt)
# print("expensive" not in txt) #True

# a = " Hello, World! "
# print(a[2:5])
# print(a[-5:-2])
# print(a.upper()) 
# print(a.lower()) 
# print(a.strip()) # returns "Hello, World!" 
# print(a.replace("H", "J"))
# print(a.split(",")) # returns ['Hello', ' World!'] 


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
