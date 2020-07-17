import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Create a new binary tree
# The root of the tree is the first element of names_1
new_tree = BSTNode(names_1[0])

# Loop through names in names_1
for name in names_1:
    # Insert each name into the tree
    new_tree.insert(name)

# Loop through names in names_2
for name in names_2:
    # Check if the tree contains the name being checked
    if new_tree.contains(name):
        # If so, add it to the duplicates list
        duplicates.append(name)

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# --- STRETCH ---
# duplicates.append(str(set(names_1).intersection(names_2)))


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
