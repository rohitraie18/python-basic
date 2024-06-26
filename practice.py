# Initialize an empty list
items = []

# Ask the user to enter items one by one
#print("Enter items for the list (type 'done' to finish):")

while True:
    item = input("Enter item: ")
    if item.lower() == 'done':
        break
    items.append(item)

# Print the unsorted list
print("Your unsorted list of items is:", items)

# Sort the list in alphabetical order
items.sort()

# Print the sorted list
print("Your sorted list of items is:", items)