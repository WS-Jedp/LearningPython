### BOOLEANS ###
# The booleans data type is always a really important data type in each language programming, in Pytho the Boolean are represent by two values:
# True and False with Capitalize characters

# Python evalutes as Boolean values each comparation or variables that have some value

if 5 > 4: # True
  print(True)

# We can convert any value into a Boolean value thanks to the constructore of the boolean data type
txt = str("Hello")
integer = int(15)
print(bool(txt)) # True
print(bool(integer))

# Is important kwno that each value that isn't empty is considered a True value, but if is empty or is 0 the value will be considered False
bool(False) # False 
bool(0) # False
bool(None) # False
bool("") # False
bool([]) # False
bool({}) # False
bool(()) # False

# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

class myClass():
  def __len__(self):
    return 0

myObj = myClass()
print(bool(myObj)) #false

## Booleans values can be returned in Functions
def myFunction:
  return True

def my_false_function:
  return False

## There is built-in methods in Python that returns Booleans value, like isinstance() which will help us to determine if some value is some data type
x = int(250)

isinstance(x, int) # True
isinstance(x, str) # False
