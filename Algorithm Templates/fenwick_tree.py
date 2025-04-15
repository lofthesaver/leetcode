'''
Binary Index Tree (BIT) - represented by an array
- Performs perfix sum query and array updates in O(log n) time

1) update(index, value): updates the value at given index 
2) query(index): gets the sum of elements from index 1 to given index
'''

# Array is 1-indexed
class FenwickTree:

    # Constructor V1: for general applications
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)


    # Updates tree[index] with given value
    def update(self, i, value):
        while i <= self.size:
            self.tree[i] += value
            i += (i & -i)


    # Gets the sum of elements from the beginning to index
    def query(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= (i & -i)
        return total
    

    # Calculates sum from left index to right index
    def range_sum(self, left, right):
        return self.query(right) - self.query(left - 1)
    

'''Test Case 1'''
# bit_tree = FenwickTree(size = 5, arr = [1, 2, 3, 4, 5])
# print(bit_tree.query(2))
# print(bit_tree.query(5))
# print(bit_tree.range_sum(1, 5))
# print(bit_tree.range_sum(2, 4))


'''Test Case 2'''
bit_tree = FenwickTree(size = 5)
nums = [0] + [1, 2, 3, 4, 5]

for i in range(1, len(nums)):
    bit_tree.update(i, nums[i])

print(bit_tree.tree)
print(bit_tree.query(2))
# print(bit_tree.query(5))
# print(bit_tree.range_sum(1, 5))
# print(bit_tree.range_sum(2, 4))




"""
Fenwick Tree - Constructor, Version 2,
for prefix sum, with optional parameter to directly provide array input

    def __init__(self, size, arr = []):

        # Set size
        self.size = size

        # Check whether array is given - if not given then use default array,
        # with all 0 values
        if not arr:
            arr = [0] * (self.size + 1)
        
        # If arr is given then directly construct the tree based on array values
        else:
            arr = [0] + arr

        self.tree = arr[:]

        # Loop through indices and update tree values
        for i in range(1, self.size + 1):
            j = i + (i & -i)
            if j <= self.size:
                self.tree[j] += self.tree[i]
"""