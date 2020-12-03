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

## Concatenate Strings
# When we use the plus operator (+) with strings we are indicating to Python to concatenate the strings, concatenatge will help us to gather multiple strins in one
txt_a = "This is the fist text."
txt_b = "This is the second text :D"
txt_c = txt_a + txt_b 
print(txt_c) # This is the first text.This is the second text :D 

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

### MODIFY A STRING ###
# Python offer us multiple built-in methods to the String object that will help us to interact and modify our strings

# the method upper() will help us to transform our string in upper case
upper_case = "upper case"
print(upper_case.upper()) # UPPER CASE

# Also there is the method lower() that will help us to transform our string into lower case
lower_case = "LOWER CASE"
print(lower_case.lower()) # lower case

# We can remove the white spaces of our string from the beginnin to the end with the method strip()
white_space = "  With  white spaces :D  "
print(white_space.strip()) # ->With  white spaces :D<-

# Replace characters of a string for anothers is really important, for that we use the method replace()
# Is important know that this method is case sensitive
# replace(oldCharacter, newCharacter, count)
txt_replace = "Hello World"
print(txt_replace.replace("H", "J")) # Jello World
print(txt_replace.replace("h", "J")) # Hello World

# We can split our strings and return a list with the multiple strings thanks to the method split()
# split(separator:Str, maxSeparator:int)
split_txt = "Juan, Esteban, Deossa, Pertuz"
print(split_txt.split(",", 2)) # ["Juan", " Esteban", " Deossa Pertuz"]
print(split_txt.split(",")) # ["Juan", " Esteban", " Deossa", " Pertuz"]

## Escape Characters
# We can escape special or illegal characters that can't be used in a normal string, this will be really helpful to write different kind of texts
# The way to do it is with the backslash :D

# illegal_txt = "There's a movie called "Interstellar" and it's AWESORE" -> This is a error
escaped_txt = "There's a movie called \"Interstellar\" and it's AWESORE" # This is cool :D

# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value
 