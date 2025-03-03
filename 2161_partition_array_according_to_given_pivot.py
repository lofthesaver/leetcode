class Solution:
    def pivotArray(self, nums, pivot):

        # Loop through array, for each element add to its respective array (less_than_pivot, equal_to_pivot, greater_than_pivot)
        less_than_pivot = []
        greater_than_pivot = []
        equal_to_pivot = 0

        for n in nums:
            if n < pivot:
                less_than_pivot.append(n)
            elif n > pivot:
                greater_than_pivot.append(n)
            else:
                equal_to_pivot += 1

        return less_than_pivot + [pivot] * equal_to_pivot + greater_than_pivot

print(Solution().pivotArray([9,12,5,10,14,3,10], 10))