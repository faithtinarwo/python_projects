# 1. Create an empty list
my_list = []

# 2. Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# 3. Insert 15 at the second position (index 1)
my_list.insert(1, 15)

# 4. Extend the list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# 5. Remove the last element
my_list.pop()

# 6. Sort the list in ascending order
my_list.sort()

# 7. Find and print the index of the value 30
index_of_30 = my_list.index(30)

# Display the final list and the index of 30
print("my_list:", my_list)
print("Index of 30:", index_of_30)