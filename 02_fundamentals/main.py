#Types 

age = 23

percent = 56.78

name = "Shubham Thorve"

human = True

print(type(age))
print(type(percent))
print(type(name))
print(type(human))

#Typecasting

c = int("100")

print(type(c))

d = str(1234)

print(type(d))

e = float(age)

print(e, type(e)) # return a new typecasted variable
print(age, type(age)) # still remains int 



# Taking input from user

my_name = input("Whats your name ??") # accepts input in string always even if you pass number it will be in string
print("Type : " + str(type(my_name)))
print("Helloo.. " + my_name)


#Comments

'''
safasgagigm
Multiline comments
afgaigag
'''


# Escape chars

print("Hello \" World \n real\tmadrid")

#working with print()

print("helloo","shubham","you","are","a","piece", "of","shit", sep="\{\}", end=".\n")

# Arithmetic Operators

print(10+10) # addition
print(10**10) #exponential
print(19//10) # floor division
print(10%7) #modulo

# Comparison Operators

print(10 <= 5)

print(10 == 5)


# Logical Operators (and / or / not) performs on boolean

print(5 == 5 and 5!=5) # True and False => False
print(5 == 5 or 5!= 5) # True or False => True

print(not(True)) # False

# Assignment Operators
x = 10
x += 5 # x = x + 5
print(x)

# Identity Operators (is / is not) checks if two variables are same or not
a = 10
b = 10
print(a is b) # True, both are same
print(a is not b) # False, both are same  

# Membership Operators (in / not in) checks if a value is present in a sequence
my_list = [1, 2, 3, 4, 5]
print(3 in my_list) # True, 3 is in the list
print(6 not in my_list) # True, 6 is not in the list

# Bitwise Operators (works on bits)
print(5 & 3) # Bitwise AND 0101 & 0011 = 0001 (only bits that are 1 in both numbers remain 1)
print(5 | 3) # Bitwise OR 0101 | 0011 = 0111 (bits that are 1 in either number remain 1)
print(5 ^ 3) # Bitwise XOR 0101 ^ 0011 = 0110 (bits that are different in both numbers become 1)
print(~5)    # Bitwise NOT 0101 = 1010 (inverts all bits, 5 becomes -6 in two's complement representation)
print(5 << 1) # Bitwise left shift 0101 ==> 1010 (shifts bits to the left)
print(5 >> 1) # Bitwise right shift 0101 ==> 0010 (shifts bits to the right)

