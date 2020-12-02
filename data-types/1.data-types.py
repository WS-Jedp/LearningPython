### DATA TYPES ###
# As we know the data types are fundamental for any programming language and the programming in general
# A data value of a variable can have a data type and a data type can do specify things
# Python have the followrings data types built-in

# Text Type = str -> String
myStr = str("Hello, this is a text")

# Numeric types = int -> Integer, float, complex
myint = int(1)
myFlt = float(2.3)
myCpx = complex(1j)

# Sequence Types = list, tuple, range
myList = list(["Multiple", "Values", 0])
myTpl = tuple(("Multiple", "Values", "As", "WEll",0))
myRng = range(6) # (0,6)

# Mapping type = dict -> Dictionary
myDict = dict({"names": "Juan Esteban", "last_names": "Deossa Pertuz"})

# Set Types = set, frozenset
mySet = set({"Hello", "There"})
myFrzSet = frozenset({"Frozen", "Set"})

# Boolean Types
myBool = bool(True)
myBoolNgt = bool(False)

# Binary Types = bytes, bytearray, memoryview
myByte = bytes(b"Hello")
myByteArr = bytearray(5)
myMemoryView = memoryview(bytes(5))