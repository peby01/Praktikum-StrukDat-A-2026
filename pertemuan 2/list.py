thislist = ["apple", "banana", "cherry"]
print(thislist)

#Allow Duplicates

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#List Length

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List Items - Data Types

list1 = ["abc", 34, True, 40, "male"]

print(list1)

#type()

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#The list() Constructor

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Access Items

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Range of Indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Check if Item Exists

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 