
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) #if it starts with "The" and ends with "Spain"


# =========================================
# email = re.compile('\w+@\w+\.[a-z]{3}')
# text = "To email Guido, try guido@python.org or guido@google.com "
# print(email.findall(text)) #['guido@python.org', 'guido@google.com']


# text = "To email Guido, try guido@python.org or guido@google.com "
# email3=re.compile(r'([\w.]+)@(\w+)\.([a-z]{3})')
# print(email3.findall(text)) #[('guido', 'python', 'org'), ('guido', 'google', 'com')]

# text = "To email Guido, try guido@python.org or guido@google.com " 
# email4=re.compile(r'(?P<user>[\w.]+)@(?P<domain>\w+).(?P<suffix>[a-z]{3})')
# match=email4.match('guido@python.org') 
# print(match.groupdict()) #{'user': 'guido', 'domain': 'python', 'suffix': 'org'}

#=============Functions==================
# Function 	Description
# findall 	Returns a list containing all matches
# search 	    Returns a Match object if there is a match anywhere in the string
# split 	    Returns a list where the string has been split at each match
# sub 	    Replaces one or many matches with a string