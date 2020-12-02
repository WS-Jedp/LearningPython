### STRINGS ###
# The strings in th programming languages are a chain of characters, we can identify string when the value is surrended of single or double quotes, in python also we can find the string with triple quotes

myStr = str("This is a string")
myStr = str('This is a string as well')
myStr = str("""This is a string in python too :D""") # The difference between this kind of string and the others, is that the triple quote is multiline, so when we break the line of characters in the string will be considered at the moment of render

myStr = str('''This kind of string can be also write with simple quotes.
So with the multile
we can break our line of text
anytime
:D
''')
print(myStr)

### STRINGS ARE ARRAYS ###
# Like many popular programming language we can see that in Python the string can be treat as arrays, this means that the strings are an array of bytes that represent a character of the unicode. However there is no a specific data-type for a character, is just a string with a length of 1
my_str = "Hello World!"
print(my_str[0]) # H

# Looping in a string
# Since strings are an Array we can looping on them with some statement of loop like for
my_loop_str = 'LOOP'
for x in my_loop_str:
  print(x)

# The Lenght Of A String
# We can find the length of a string with the built-in method len()
my_lenght = "life"
print(len(my_lenght)) # 4

# Checking In A String
# We can verify if some characters or words are in some of our strings or not
my_paraphrase = "Hello, beatiful world, welcome to Python :D"
print("world" in my_paraphrase) # true
print("universe" in my_paraphrase) # false
print("javascript" not in my_paraphrase) # true


### SLICING ###
# In Python we can return a range of character of some string with a special syntaxis called slice syntax
# This syntax will help us to go over for some string and know his characters
# The slice syntax receive first the index where we want to start slice our string and the index where we want to finish of slice our string
# The index that we write aren't included in the slice

my_slice_str = "oro"
print(my_slice_str[1:2]) # r
print(my_slice_str[0:3]) # oro
print(my_slice_str[:3]) # oro # Slice from the beggining
print(my_slice_str[0:]) # oro # Slice until the end

my_slice_two = "two"
# We can use negative indexes to start from the end the slice
print(my_slice_two[-3:-1]) # tw
print(my_slice_two[-1:]) # o
