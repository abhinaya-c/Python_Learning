print('Hello')
print("hello")

a = 'Hi, world'
print(a)

#Multi-line array
b = """python is very useful language,
can be used for many purposes"""
print(b)

#string as a array
x = "Hello, World!"
print(x[0])

#looping through a string array

for x in "banana":
    print(x)

#string length

a = "Hello, World!"
print(len(a))

#check string
txt ="The best thing in life are free!"
print("free" in txt)

#use it in an if statement
if "free" in txt:
    print("Yes, 'free' is present.")

#check if Not 
print("expensive" not in txt)

if "expensive" not in txt:
    print("No, 'expensive' is not present.")



#Slicing Strings

b = "Hello, World!"
print(b[2:5]) #get character form position 2 to 5

print(b[:5]) #get character form start to position 5

print(b[2:]) #slice to the End

#Use the negative indexing

print(b[-7:-2])
