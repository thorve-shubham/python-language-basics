# If else statements in Python

age = int(input("Enter your age: ")) 

if(age > 18):
    print("You are an adult.")
elif(age == 18):
    print("You just about age.")
else:
    print("You are a minor.")

# Match case statements in Python

my_name = input("Enter your name: ")

match(my_name):
    case "Shubham":
        print("Hello Shubham!")
    case "John":
        print("Hello John!")
    case _:
        print("Hello stranger!")

# For loop in Python

for i in range(1,5): # range(start, stop) generates numbers from start to stop-1
    print("Iteration:", i)

# While loop in Python

while i < 10:
    print("Current iteration:", i)
    i += 1  # Increment i to avoid infinite loop

# While loop with break and continue
i = 0
while i < 10:
    i += 1
    if i == 5:
        print("Skipping 5")
        continue  # Skip the rest of the loop when i is 5
    if i == 8:
        print("Breaking at 8")
        break  # Exit the loop when i is 8
    print("Current number:", i)


# Pass statement in Python
for j in range(1, 6):
    if j == 3:
        pass  # Do nothing for j == 3
    else:
        print("Current number:", j)




