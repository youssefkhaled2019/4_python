
# ==================List []============================
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(*list("love apple"))
# print(thislist) 
# print(*thislist) #apple banana cherry
# print(len(thislist)) 
# thislist = list(("apple", "banana", "cherry"))

# print(thislist[1]) 
# print(thislist[-1]) 
# print(thislist[2:5]) 
# print(thislist[-4:-1])
# print (x[::2])
# print (x[0][0])

# Change Item Value

# thislist[1] = "blackcurrant"
# thislist[1:3] = ["blackcurrant", "watermelon"] #replace 1,2

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
#["apple", "blackcurrant", "watermelon", "cherry"]

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"] # ['apple', 'watermelon']

# a,n = ['a', 'b', 'c'], [1, 2, 3]
# x = [a, n]
# a*5 #repet list


# x = [0] * 1000 # x = [0.0] * 1000
# x = [[0]*8] *10





#  ***************** (Join )Append-insert-extend *******************


# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange") # ['apple', 'banana', 'cherry', 'orange']
# thislist.insert(0, "orange") #['orange', 'apple', 'banana', 'cherry']

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
#['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
# xx=thislist+tropical
# ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)#['apple', 'banana', 'cherry', 'kiwi', 'orange']



# x=[1,2,3,4,5]
#x.append([1,2,4])[1, 2, 3, 4, 5, [1, 2, 4]]
#x.append(1) [1, 2, 3, 4, 5, 1]
#x.extend([1,2,4]) [1, 2, 3, 4, 5, 1, 2, 4]


#  ***************** Remove *******************
# t[:]=[]
# t[2:5]=[]
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# thislist.pop(0) #remove first item
#  thislist.pop() #Remove the last item:
# thislist.clear()
# del thislist[0]
# del thislist  deleted "thislist" variable 

#  ***************** loop *******************

# for x in thislist:
#   print(x) 

# for i in range(len(thislist)):
#   print(thislist[i]) 

# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# [print(x) for x in thislist] #??


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)     




# newlist = [ x**3 for x in range(12)]
# newlist = [3*x for x in [y**2 for y in range(10)]]
# newlist = [x for x in fruits if "a" in x]
# newlist = [x for x in fruits if x != "apple"]   #??
# newlist = [i for i in range(20) if i%3 ==0  and i %2 ==0 ]
# newlist  = [(i,j) for i in range(3) for j in range(4)]
# newlist = [[0 for i in range(5)] for j in range(7)]
# newlist = [x if x != "banana" else "orange" for x in fruits]  #??
# newlist = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(newlist) 



# y = list(map(lambda x : x**3 , range(12)))





# from operator import itemgetter ,methodcaller

# student_tuples = [('john', 'A', 15),('jane', 'B', 12),('dave', 'B', 10),]
# print(sorted(student_tuples, key=itemgetter(2)))#index 2  ,, key=itemgetter(1,2)
# print(sorted(student_tuples, key=itemgetter(1,2)))

# messages = ['critical!!!', 'hurry!', 'bla bla', 'alabama'] 
# print (sorted(messages, key=methodcaller( 'count', 'a')))

# # =====================enumerate===========================
# my_list = ['apple', 'banana', 'grapes', 'pear'] 
# for c, value in enumerate(my_list, 1): 
#     print(c, value)
# # ======================zip==========================
# alist = ['a1', 'a2', 'a3'] 
# blist = ['b1', 'b2', 'b3'] 
# for a, b in zip(alist, blist):
#     print (a, b)


#  ***************** sort-reverse *******************

# thislist.sort()
# thislist.sort(reverse = True)

# Sort the list based on how close the number is to 50:
# def myfunc(n):
#   return abs(n - 50)
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)

# By default the sort() method is case sensitive,
#  resulting in all capital letters being sorted before lower case letters:
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# thislist.sort(key = str.lower)  #??
# thislist.reverse()


# y=[1,2,3,4,5,6,7]
# len (y)
# sum(y) #print(sum([k for k in range(20)]))
# max(y)
# min(y)
# sorted(y)

# y=[('F', 9), ('Cl', 17), ('Br', 35), ('I', 53), ('At', 85)] 
# sorted(y, key=lambda e: e[1])#reverse = True

#  ***************** Copy *******************

#Copy 
# mylist = thislist.copy()
# mylist = list(thislist)
# mylist = thislist[:]


# Join Lists

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# list3=[list1,list2]

# for x in list2:
#   list1.append(x)

# list1.extend(list2)  

#  ***************** Methods *******************
y=[1,2,3,4,5,6,7]

y.count (555)
y.index (5)

y.reverse()
list(range(20))



# List Methods

# Python has a set of built-in methods that you can use on lists.
# Method 	    Description
# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the item with the specified value
# reverse()     Reverses the order of the list
# sort()	    Sorts the list