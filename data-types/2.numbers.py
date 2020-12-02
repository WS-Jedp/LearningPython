### NUMBERS ###
# As we can see in Python exists three numberic types, integers (int), floating numbers (float) and complex numbers (complext)

# Integer
# A integer number is a whole number, positive or number, without decimals of unlimited lengths
myInt = int(135153)
print(type(myInt))# <class of int>

myInt = int(-135153) 
print(type(myInt))# <class of int>

myInt = int(12)
print(type(myInt))# <class of int>

# Float
# A floating point number is a number, positive or negative that contians one or more decimals
myFlt = float(2.3)
print(type(myFlt)) # <class float>

myFlt = float(-2.3)
print(type(myFlt)) # <class float>

myFlt = float(2.45)
print(type(myFlt)) # <class float>

myFlt = float(3.65489)
print(type(myFlt)) # <class float>

# An important functionality of the floating numbers is the character "e", that will help us to create scientific numbers indicating the power of 10
myFlt = float(2.36e10) 
print(type(myFlt)) # <class float>

# Complex
# We can create complext numbers with Python with the character "j" representing the imaginary part
myCpx = complex(5j)
print(type(myCpx)) # <class 'complex'>

myCpx = complex(3+5j)
print(type(myCpx)) # <class 'complex'>

# Random Number
# Python by himself doesn't bring a built-in function of generate a random number, but we can ipmort a built-in module that will help us to create reandom numbers
import random
print(random.randrange(1,10))


### Conversion ###
# We can convert the data value of variable into another data type with the constructors of each data type
myFlt = float(2.3)
print(type(myFlt)) # <class 'float'>

myInt = int(myFlt)
print(type(myInt)) # <class 'int'>