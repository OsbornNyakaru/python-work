# Creating an empty list called my_list
my_list = []

# Appending the elements to my_list: 10, 20, 30, and 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting value 15 at the 2nd position
my_list.insert(1, 15)

# Extend my_list with list: [50, 60, 70]
my_list.extend([50, 60, 70])

# Removing last element from my_list
my_list.pop()

# Sorting in ascending order
my_list.sort()

# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of 30 in my list:", index_of_30)

# Final my_list output
print("Final my_list:", my_list)
