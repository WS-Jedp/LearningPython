### STRINGS FORMAT ###
# In Python we can't concatenate a string with a number with the plus operators (+)

## ERROR
# age = 36
# txt = "My name is Jhon and  I'm " + age
# print(txt)
##

# But for this kind of situations Python offer us the built-in method format() for the strings Objects
# format(...arguments)

# This method will help us to replace the placeholders that we put in a strings with the arguments that we specify
# The placesholders are created with empty brackets or with the index of the arguments that must be 

txt = "My name is {0} and I'm {1}"
print(txt.format("Juan", 19)) # My name is Juan and I'm 19
