### OPERATORES ###
# The operators are used to perfom operation on variables and values
# According to each data type the operactor can be different

x = 10
y = 5

print(x + y) # 15

# Still, Python divides th operators in multiple groups

## Aritmethic Operators

# Operator | Name | Example
# + | Addition | 2 + 3
# - | Substraction | 2 - 3
# * | Multiplication | 2 * 3
# / | Division | 2/3
# // | Floor Division | 10 // 2 # 5
# % | Modulus | 2 % 3
# ** | Exponentiation | 2 ** 3

## Assigment Operators

# Operator | Example | Same As
# = | x = 5 | x = 5
# += | x += 5 | x = x + 5
# -= | x -= 3 | x = x - 3
# *= | x *= 2 | x = x * 2
# /= | x /= 2 | x = x / 2
# %= | x %= 2 | x = x % 2
# //= | x //= 3 | x = x // 3
# **= | x **= 4 | x = x ** 4
# &= | x &= 2 | x = x & 2
# |= | x |= 5 | x = x | 5
# ^= | x ^= 2 | x = x ^ 2
# >>= | x >>= 1 | x = x >> 1
# <<= | x <<= 1 | x = x << 1

## Compartaion Operators // The comparation Operators return always a Boolean value according to the result of the comparation
# Operators | Name | Example  
# == | Equal | x == 2
# != | Not Equal | x != 3
# > | Greater Than | x > 2
# < | Less Than | x < 3
# >= | Greater Than Or Equal | x >= 3
# <= | Less Than Or Equal | x <= 2

## Logical Operators
# These operators are used to combine multiple conditional statements
# Operator | Description | Example
# and | Return True if the two conditions are True | x > 10 and x < 20
# or | Return True if one of the two or both conditions are true | x > 10 or x < 20
# not | Reverse the result, return False if the result is true | not(x > 10)

## Identity Operators
# The Identity Operators will help us to compare the identity of the Objects, this means not only the value that have the variables, this means compare if the variables are the same Object in memory location
# Operator | Description | example
# is | Will return True if both variables are the same Object | x is y
# is not | Will return True if both variables aren't the same | x is not y

## Membership Operators
# Are used to test if a sequence is presented  in an Object, so we can verify if some elements is in some Object
# Operator | Description | Example
# in | Returns True if the sequence is present in the Obejct | x in y
# not in | Returns False if the sequence isn't present in the Obejct | x not in y

## Bitwise Operators
# These operators are used to compare (binary) numbers
# operator | name | description
# & | AND	| Sets each bit to 1 if both bits are 1
# |	| OR | Sets each bit to 1 if one of two bits is 1
# ^	| XOR	| Sets each bit to 1 if only one of two bits is 1
# ~ | NOT | Inverts all the bits
# << | Zero fill left shift	| Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>| Signed right shift | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off