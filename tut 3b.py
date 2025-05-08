#Question 1
# Initializing an empty list
char_list = []

# Using a while loop to repeatedly take user input
while True:
    char = input("Enter one char: ")
    if char.lower() == "quit":  # Checking for "quit" to stop
        break
    char_list.append(char)

# Displaying the filled list and its size
print("List:", char_list)
print("List size is:", len(char_list))





#question 2
# Initializing an empty list
char_list = []

# Using a while loop to repeatedly take user input
while True:
    char = input("Enter one char: ")
    if char.lower() == "quit":  # Checking for "quit" to stop
        break
    char_list.append(char)

# Displaying the filled list and its size
print("List:", char_list)
print("List size is:", len(char_list))


#question 3
# Function using non-keyword arguments (*args)
def print_list_items(*args):
    for item in args:
        print(item)

# Initializing an empty list
char_list = []

# Using a while loop to repeatedly take user input
while True:
    char = input("Enter one char: ")
    if char.lower() == "quit":  # Checking for "quit" to stop
        break
    char_list.append(char)

# Displaying the filled list and its size
print("List:", char_list)
print("List size is:", len(char_list))

# Using the non-keyword argument function to print list items
print_list_items(*char_list)
