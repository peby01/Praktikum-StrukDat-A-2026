#Strings

print("carat")
print('idubilu')

#Quotes Inside Quotes

print("gwenchana girls")
print("mereka dijuluki 'sikembar'")
print('she say "wowww your so cool!"')

#Assign String to a Variable

a = "pretty"
print(a) 

#Multiline Strings

a = """I feel like the possibility of 
all those possibilities being possible 
is just another possibility that 
can possibly happen."""
print(a) 

#Slicing

b = "annyeong, chingu!"
print(b[3:7])

#Slice From the Start

b = "annyeong, chingu!"
print(b[:3])

#Slice To the End

b = "annyeong, chingu!"
print(b[5:])

#Negative Indexing

b = "aquarius, pisces"
print(b[-7:-3])

#Upper Case

a = "Aquarius, Pisces"
print(a.upper())

#Lower Case

a = "Aquarius, Pisces"
print(a.lower())

#Remove Whitespace

a = " say the name! "
print(a.strip()) # returns "say the name!" 

#Replace String

a = "say the name!"
print(a.replace("y", "e"))

#Split String

a = "ni hao, gege"
print(a.split(",")) # returns ['ni hao', ' gege'] 

#String Concatenation

a = "seven"
b = "teen"
c = a + b
print(c)

a = "ni hao"
b = "jiejie"
c = a + " " + b
print(c)#

#F-Strings

age = 19
txt = f"My name is peby, I am {age}"
print(txt)

#Placeholders and Modifiers

harga = 90
txt = f"harganya {harga} ribu"
print(txt)

price = 85
txt = f"barang ini di jual {price:.3f} ribu"
print(txt)

txt = f"The price is {17 * 23} yen"
print(txt)




