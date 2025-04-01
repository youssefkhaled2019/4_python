
# x = lambda a : a + 10
# x = lambda a, b : a * b
# x = lambda a, b, c : a + b + c

# def myfunc(n):
#   return lambda a : a * n 

# print(x(5)) 
# print(x(5, 6)) 
# print(x(5, 6, 2)) 


# mydoubler = myfunc(2)
# mytripler = myfunc(3)
# print(mydoubler(11))
# print(mytripler(11))




powers = [lambda x: 1,lambda x: x,lambda x: x**2,lambda x: x**3] 
print(powers[0](5))   
print(powers[1](5))   
print(powers[2](5))   
print(powers[3](5))   
# =====================map===========================
y = list(map(lambda x : x**3 , range(12)))


list(map(float, range(12)))


mylist = (0,1,2,3,4,5,6,7,8,9) 
list(map(lambda x: x**2 , mylist))



list1 = (1,2,3,4,5,6) 
def cpower (x): 
    return x**3 
print (list(map(lambda x :cpower(x)  , list1)))
# ====================filter============================
mylist = [0,1,2,3,4,5,6,7,8,9] 
evennumber = list(filter(lambda x: x % 2 == 0 , mylist   )) 
oddnumber = list(filter(lambda x: x % 2 == 1 , mylist   )) 
print (evennumber) 
print (oddnumber) 




# ================================================



# ================================================

I = iter([2, 4, 6, 8, 10])  #iter(range(20))
print(next(I)) 
print(next(I))

#------------------------

def yie(): 
    for i in range(10): 
        yield i          
for g in yie(): 
       print(g)
#------------------------
def yie():
 for i in range(10):
     yield i
 
f = yie()
for i in range (5):
    print (next(f))
# print (next(f))
# print (next(f))   
# print (next(f))   
#------------------------
## Fibonacci
def fibon(n):  #
    a = b = 1 
      
    for i in range(n): 
        yield  a 
        a , b = b , a+b 
      
for x in fibon(20): 
    print (x)