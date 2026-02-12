#
thisset = {"apple", "banana", "cherry"}
print(thisset) 

#Get the Length of a Set

thisset = {"apple", "banana", "cherry"}

print(len(thisset)) 

#Set Items - Data Types

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

#type()

myset = {"apple", "banana", "cherry"}
print(type(myset))

#The set() Constructor

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 

#
#Access Items

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x) 

#Add Items

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset) 

#Add Sets

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset) 

#Add Any Iterable

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset) 