### VARIABLES ###
# The variables are containers for storing data values
# In python the creation of variables are really easy, it happens when we assign a value to it with the "=" symbol

x = 0
y = "Number :D"

# The variables don't need to declare his data type and can even change of data type in after of been set

x = "The variable X is now a string"

### CASTING ###
# If we like and want to declare the data type of our variables we can use the casting of Python
"""
  The casting of Python works with three primitive data tpyes:
  x = str(3) -> String = x will be '3' 
  y = int(2) -> Integer = y will be 2
  z = float(5) -> Float = z will be 5.0 
"""

name = str("Juan Esteban Deossa Pertuz")
name = 2 # Still we can change his data type without any problem
print(name)

### GET THE TYPE ###
# We can get the type of our variables with the built-in function type(variable)
number = 5
print(type(number)) # <class 'int'>
string = str("Hello world")
print(type(string)) # <class 'str'>

### Single Or Double Quotes? ###
# In python this doesn't matter, we can use the quotes that we prefer
single = 'Hello there :D'
double = "Hello there but with double"

### CASE SENSITIVE ###
# THe variables of Python are case sensitive, this means that we can have multiple variable with the same characters but with different case in each one and python will considered the variabless different of the others
hello = "This is hello!"
Hello = "This is different to hello"
print(Hello)

### Assign Multiple Values ###
# We can assing multiple values to multiple variables dynamically
# Is really important to have the same quantity of variables that the same quantity of values that we want to assing
x, y, z = "Orange", "Banana", "Cherry"
print(x) # Orange
print(y) # Banana
print(z) # Cherry

# We also can assing a single value to multiple variables
x = y = z = "Fruit"
print(x) # Fruit
print(y) # Fruit
print(z) # Fruit

### Unpack a Collection ###
# If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.
fruits = ["Orange", "Banana", "Cherry"]
x, y, z = fruits
print(x) # Orange
print(y) # Banana
print(z) # Cherry


### OUTPUT VARIABLES ###
# When we use the print built-in method of python we can output multiple values, when we want to make an output of a string we can use multiple operators to interact with our variables at the moment of make the outpu
myStr = "Python is"
my2ndString = "awesome"
print(myStr + " " + my2ndString) # Python is awesome

# But when we are working with number data tpyes the operators will work for us as mathematical operators
myInt = 3
my2ndInt = 5
print(myInt + my2ndInt) # 8
