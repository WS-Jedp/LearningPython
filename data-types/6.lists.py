### LISTS ###
# Python Lists are used to store multiple values in one single variable.
# The Lists are one of the 4 built-in data types of Python that used to store collectiosn of data. The other 3 are the Tuples, Sets and Dictionaries, each one with his own features and usuabilities.

# The lists are created with the square brackets, can contain all tpye of data type and can be duplicated, his values will be ordered by the indexes that start in 0 and increase according to the numbers of the elements that contains
# The lists have a order that we can change, but in the most of time the order wont change at least we specified what.
# The list are changeable, so this means that we can chaneg the value that contains, add or remove more values with some methods that Python offer us

my_first_list = ["hello", "world", 2020]

# As we know, each item is pointed with his index value that starts in 0 in the first value
my_first_list[0] # "hello"

## Length 
# In the majority of our programms will be really helpful know the quanity of items and values that have a lists, fot that we can use the built-in method of Python len() that will help us to know the quantity of items that have a list.
print(len(my_first_list)) # 3

# So for the point of view of Python a List is a Object of the class <list> and we can use his constructore to build our lists.
# Can be created with the constructors in two ways:
another_list = list(["Hello", "There"])
another_list_2 = list(("Hello", "There"))
print(another_list_2)
print(another_list_3)