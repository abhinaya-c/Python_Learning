#Variables:
#varibles are containerd for storing data values.

#Creating Variables:
#Example:

x = 5
y = "WRC"
print(x)
print(y)

#Changing Type after they have beem\n set.
x = 4          #x is of type int 
x = "NesCafe"  #x is now of type str
print(x)

#CASTING AND GET TYPE

x = str(3)   # x will be '3'
y = int(3)   # y will be 3
z = float(3) # z will be 3.0

#Get type

print(type(x))
print(type(y))
print(type(z))

#Single or Double Quotes?

x = "James"
# Both are same 
x = 'James'

#Case-Sensitive
#variable names are case-sensitive.

#This will create two variables:
a = 4
A = "Simon"
# A will not overwrite a 
print(a)
print(A)

#Python - Variable Names:
#Legal variables names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Multi-Words Variables Names
#Camel Case:
myVariableName = "John"

#Pascal Case:
MyVariableName = "John"

#Snake Case:
my_variable_name = "John"

#ASSIGN MULTIPLE VALUES
  # - Many Values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

 # - One Value to Multiple Variables
p = q = r = "Orange"
print(p)
print(q)
print(r)

# UNPACK A COLLECTION
# If you have a collection of values in a list, tuple etc. Python allows the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(a)
print(b)
print(c)