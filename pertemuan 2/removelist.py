#Remove Specified Item

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove Specified Index

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Clear the List

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Loop Lists
#Loop Through a List

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 

#Loop Through the Index Numbers

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) 

#Using a While Loop

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#Looping Using List Comprehension

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] 