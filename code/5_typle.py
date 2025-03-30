
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.



# =================================Tuples ()====================================
# A tuple is a collection which is ordered and unchangeable.
# Tuple items are [ordered], [unchangeable], and [allow duplicate] values.
# Tuple items are indexed, the first item has index [0], the second item has index [1]
# Ordered
   # When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Unchangeable
   # Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.


# mytuple = ("apple", "banana", "cherry", "apple", "cherry")
# # tuple1 = ("abc", 34, True, 40, "male") 

# # thistuple = ("apple",) # a tuple
# # print(type(thistuple))
# # thistuple = ("apple") #NOT a tuple is str
# # print(type(thistuple)) 

# # thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets

#  ***************** Access *******************

# print(mytuple[1])
# print(mytuple[-1])
# print(mytuple[2:5])
# print(mytuple[-4:-1])


# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple") 


#  ***************** Update  *******************

# # Update Tuples
# # Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

# # Add Items
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# # or
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)


# # Remove Items
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# # or
# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exist








# fruits = ("apple", "banana", "cherry") #packing     # When we create a tuple, we normally assign values to it. This is called "packing" 
# (green, yellow, red) = fruits             # we are also allowed to extract the values back into variables. This is called "unpacking":


# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")  # Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list. 
# (green, yellow, *red) = fruits 

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# (green, *tropic, red) = fruits #?? # If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.






# Loop Through a Tuple
# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x) 

# for i in range(len(thistuple)):
#   print(thistuple[i]) 

# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1   

#  ***************** sort  *******************
student_tuples = [('john', 'A', 15),('jane', 'B', 12),('dave', 'B', 10)] 
a = sorted(student_tuples, key=lambda student: student[2])
#  ***************** Join  *******************

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)
# tuple3 = tuple1 + tuple2  #??


fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2 #Multiply Tuples

#  ***************** Methods  *******************

print(fruits.count("apple"))
print(fruits.index("apple"))