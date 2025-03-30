

# ========================Operators======================
# https://www.w3schools.com/python/python_operators.asp
# Arithmetic operators 
     #     (+,-,*,/,%,**,//)
# Assignment operators
#    x = 5
#    x += 3  #  (+,-,*,/,%,**,//)
#    x &= 3   #5=101 ,3=011   101&011=001 -> 1 and
#    x |= 3   #5=101 ,3=011   101|011=111 -> 7  or
#    x ^= 3   #5=101 ,3=011   101|011=110 -> 6  xor
#    ~3    3 = 0000000000000011 -> -3 = 1111111111111101
#    x >>= 3  #5=101 ->000101 -> 000=0
#    x >>= 2  #5=101 ->00101  -> 001=1
#    x >>= 1  #5=101 ->0101   -> 010=2

#    x <<= 3  #5=101 ->101000 -> 101000=40
#    x <<= 2  #5=101 ->10100  -> 10100=20
#    x <<= 1  #5=101 ->1010   -> 1010=10

#    print(x := 3) #3

# Comparison operators (==,!=,>,<,>=,<=)
# Logical operators  (and ,or,not)
    # -) x < 5 and  x < 10
    # -) not(x < 5 and x < 10)
# Identity operators  (is ,is not )
          # -) x is y
          # -) x is not y
# Membership operators (in  ,not in )
          # -) x in y
          # -) x not in y
# Bitwise operators
     # Operator 	Name 	               Description 	Example 	Try it
     # &  	     AND 	                    Sets each bit to 1 if both bits are 1 	x & y 	
     # | 	          OR 	                    Sets each bit to 1 if one of two bits is 1 	x | y 	
     # ^ 	          XOR 	                    Sets each bit to 1 if only one of two bits is 1 	x ^ y 	
     # ~ 	          NOT 	                    Inverts all the bits 	~x 	
     # << 	     Zero fill left shift 	Shift left by pushing zeros in from the right and let the leftmost bits fall off 	x << 2 	
     # >> 	     Signed right shift 	     Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off 	x >> 2


#=========================================================
# print(~3)
"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""
#========================[Operator precedence]=================================
#Operator precedence describes the order in which operations are performed.
# Operator 	                                   Description 	Try it
# () 	                                        Parentheses 	
# ** 	                                        Exponentiation 	
# +x  -x  ~x 	                                   Unary plus, unary minus, and bitwise NOT 	
# *  /  //  %                                     Multiplication, division, floor division, and modulus 	
# +  - 	                                        Addition and subtraction 	
# <<  >> 	                                        Bitwise left and right shifts 	
# & 	                                             Bitwise AND 	
# ^ 	                                             Bitwise XOR 	
# | 	                                             Bitwise OR 	
# ==  !=  >  >=  <  <=  is  is not  in  not in  	Comparisons, identity, and membership operators 	
# not 	                                        Logical NOT 	
# and 	                                        AND 	
# or 	                                        OR