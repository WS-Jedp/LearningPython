### GLOBAL VARIABLES ###
# When we create a variable outside of a function or a block of code, are known as global variables
# The global variables can be used anytime and anywher without matter the block code or scope

x = "I'm"

def greeting():
    print(x + " a software engineer!")

greeting()

# The variables that are created inside of a function will kwnon as local variables and can have the same name of the global variables, but are different
# The big difference between the global and local variables, is that the local variables can only be use inside of the function or block code that was created it

def local():
    x = "This x is different!"
    print(x)

local()

### Global Keyword ###
# When we are working with local variables we can make of these global variables with the global keyword, helping us to make our local variable global
def makeGlobal():
    global x
    x = "We're"

def makeYGlobal():
    global y
    y = "We're H U M A N S"

makeGlobal()
makeYGlobal()
greeting()
print(y)
