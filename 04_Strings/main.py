name = 'Shubham Thorve'

print(name)

name1 = """Shubham Thorve
Is a pussy """ # Multiline string

print(name1) # First character

truth = '''Real Marid
Is the best team in the world''' # Multiline string

print(truth)

# String indexing and slicing
print(name[0]) # First character
print(name[-1]) # Last character
print(name[0:7]) # Slicing from index 0 to 6
print(name[7:13]) # Slicing from index 7 to 12
print(name[:7]) # Slicing from start to index 6
print(name[8:]) # Slicing from index 8 to end
print(name[::2]) # Slicing with step 2 skips every second character
print(name[::-1]) # Reversing the string

print(name[-1:-4:-1])

print(name[2:-1])


print(name[::-2]) # Reversing the string with step 2 skips every second character
print(name[1:-1:2]) # Slicing from index 1 to -1 with step 2

print(name[2::-1])

# String methods adn functions

# string are immutable in python means you cannot change the string once created but you can create a new string with the changes you want to make

name = "shubhamthorve"

# name[0] = 's' # This will give error TypeError: 'str' object does not support item assignment

length = len(name) # length of the string
print(length)

print(name.lower()) # convert to lowercase
print(name.upper()) # convert to uppercase
print(name.title()) # convert to title case
print(name.capitalize()) # capitalize the first character
print(name.count('h')) # count the number of occurrences of a character
print(name.find('h')) # find the index of the first occurrence of a character
print(name.replace('h', 'H')) # replace a character with another character
print(name.isalpha()) # check if the string contains only alphabets
print(name.isdigit()) # check if the string contains only digits
print(name.isalnum()) # check if the string contains only alphanumeric characters
print(name.startswith('Shu')) # check if the string starts with a substring
print(name.endswith('ham')) # check if the string ends with a substring
print(name.split('h')) # split the string into a list of substrings
print('-'.join(['Shubham', 'Thorve'])) # join a list of strings

title = "   shubham thorve   "
print(title)
print(title.strip()) # remove leading and trailing whitespace
print(title.lstrip()) # remove leading whitespace
print(title.rstrip()) # remove trailing whitespace
print(title.replace(" ", "")) # remove all whitespace

#String formatting

name = "Shubham"
age = 20
print("My name is " + name + " and I am " + str(age) + " years old.") # concatenation

print("My name is {} and I am {} years old.".format(name, age)) # format method
print(f"My name is {name} and I am {age} years old.") # f-string (Python 3.6+)
print("My name is {name} and I am {age} years old.".format(name=name, age=age)) # format method with keyword arguments

# ord and chr functions

print(ord('a')) # ASCII value of a character
print(chr(97)) # character from ASCII value