"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

# class BinarySearchTree:
#     def __init__(self, root=None):
#         self.root = root

# ^^^-- is the same as --vvv

# root = BSTNode(26) # Root is 26

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Compare the input value with the value of the Node
        # if value < Node's value
        if value < self.value:
            # We need to go left
            # if we see that there is no left child...
            if self.left is None:
                # wrap the value in a BSTNode and park it
                self.left = BSTNode(value)
            # otherwise, there is a child
            else:
                # call the left child's `insert` method
                self.left.insert(value)
        # otherwise, value >= Node's value
        else:
            # we need to go right
            # if we see that there is no right child...
            if self.right is None:
                # wrap the value in a BSTNode and park it
                self.right = BSTNode(value)
            # otherwise, there is a child
            else:
                # call the right child's `insert` method
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Check if the target is equal to the current node's value
        if target == self.value:
            return True
        # Check if the left side exists and
        # if the target is less than the current node's value
        elif self.left and target < self.value:
            return self.left.contains(target)
        # Check if the right side exists and
        # if the target is greater than the current node's value
        elif self.right and target > self.value:
            return self.right.contains(target)
        # Otherwise, the target value doesn't exist in this tree
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # Check if there's a right node
        if self.right:
            # Recursion to the right
            return self.right.get_max()
        # Once there is no longer a right child
        # We are at the right-most value, which is max
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # By checking the left before even setting the recursive function
        # This will put things in descending order

        # Check if there's a left node
        if self.left:
            # Recursion to the left
            self.left.for_each(fn)

        # The recursive function:
        fn(self.value)

        # Check if there's a right node
        if self.right:
            # Recursion to the right
            self.right.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # By checking the left before even setting the recursive function
        # This should put things in descending order

        # Reference the current node
        current = node

        # Check if there's a left node
        if self.left:
            # Recursion to the left
            self.left.in_order_print(current.left)

        # The recursive function:
        print(current.value)

        # Check if there's a right node
        if self.right:
            # Recursion to the right
            self.right.in_order_print(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        from collections import deque

        # We'll use a queue to facilitate the ordering
        queue = deque()
        queue.append(self) # self = root node

        # continue to traverse as long as
        # there are nodes in the queue
        while len(queue) > 0:
            # pop the top node from the queue
            current = queue.popleft()

            # add the current node's left child first
            if current.left:
                queue.append(current.left)

            # add the current node's right child
            if current.right:
                queue.append(current.right)
            
            # call the anonymous function
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # We'll use a stack
        stack = []
        stack.append(self) # self = root node

        # If stack has nodes in it
        # There are more nodes to traverse
        while len(stack) > 0:
            # pop the top node from the stack
            current = stack.pop()

            # add the current node's right child first
            if current.right:
                stack.append(current.right)

            # add the current node's left child
            if current.left:
                stack.append(current.left)

            # call the anonymous function
            print(current.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # Call previously-created method for easy solution
        self.dft_print(node)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # Reference the current node
        current = node

        # Check if there's a left node
        if self.left:
            # Recursion to the left
            self.left.post_order_dft(current.left)

        # Check if there's a right node
        if self.right:
            # Recursion to the right
            self.right.post_order_dft(current.right)

        # The recursive function:
        print(current.value)
