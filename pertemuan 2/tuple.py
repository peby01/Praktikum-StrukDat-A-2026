thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Tuple Length

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Create Tuple With One Item

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) 

#Tuple Items - Data Types

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

#type()

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#The tuple() Constructor

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#Access Tuple Items
#Access Tuple Items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Negative Indexing

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Range of Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#Range of Negative Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Check if Item Exists

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") 
