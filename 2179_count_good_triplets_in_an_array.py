from typing import List

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
    

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        # Make a mapping for number --> index of nums2
        nums2_mapping = {}
        for i, v in enumerate(nums2):
            nums2_mapping[v] = i

        # Make a mapping for the index in nums2 to the index of that value in nums1
        pos2_to_pos1_mapping = {}
        for i, v in enumerate(nums1):
            pos2_to_pos1_mapping[nums2_mapping[v]] = i

        # 2. Create Fenwick tree
        tree = FenwickTree(len(nums1))
        # Record result
        res = 0

        # 3. For each index in nums2, find the corresponding index in nums1 (both indices are the same number),
        # find the number of values to the left of this position, and add 1 to this position,
        # then find the number of elements that are to the right, and add left * right to result
        for pos2 in range(len(nums2)):

            # Index of nums2[pos2] in nums1
            pos1 = pos2_to_pos1_mapping[pos2]

            # Query the number of values to the left of this index
            left_values = tree.query(pos1)

            # Update the number of values at this index (tree is 1-indexed, so add 1)
            tree.update(pos1 + 1, 1)

            # Calculate the number of elements to the right 
            # (len(nums2) - 1 - pos1) is the total number of indices greater than pos1,
            # pos2 - left_values are the indices on the left
            right_values = (len(nums2) - 1 - pos1) - (pos2 - left_values)

            # Add to res
            res += left_values * right_values

        return res
    
    
print(Solution().goodTriplets(nums1 = [2,0,1,3], nums2 = [0,1,2,3]))
print(Solution().goodTriplets(nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]))