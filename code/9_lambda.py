
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
# ================================================
y = list(map(lambda x : x**3 , range(12)))








# ================================================

I = iter([2, 4, 6, 8, 10]) 
print(next(I)) 
print(next(I))

