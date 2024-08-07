#PYHTON DATA TYPES

#Buit-in Data types

# Text type : str
# Numeric types : int , float , complex
# sequence types: list , tuple, range 
# Mapping types: dict 
# set types: set, frozenset
# Boolean type: bool
# Binary type: NameType

#Example:
x = 5
print(type(x))

#Setting the data types 

# x = "Hello World!" -> str
# x = 20 -> int
# x = 20.5 -> float
# x = 1j -> complex
# x = ["apple", "banana", "orange"] -> list
# x = ("apple", "banana", "orange") -> tuple
# x = range(6) -> range
# x = {"apple" : "John", "age" : 36} -> dict
# x = {"aaple", "banana", "cherry"} -> set
# x = frozenset({"apple", "banana", "cherry"}) -> frozenset
# x = True -> bool
# x = b"Hello" -> bytes
# x = bytearray(5) -> bytearray
# x = memoryview(bytes(5)) -> memoryview
# x = None -> NoneType

x = "Hello World!"
print(type(x))

#Type Conversion

x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Random Numner Concept
import random
print(random.randrange(1,10))


