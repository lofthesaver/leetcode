from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

        # 1. Count the number of zeros in both arrays
        nums1_zeros, nums2_zeros = 0, 0

        for v in nums1:
            if v == 0:
                nums1_zeros += 1
        
        for v in nums2:
            if v == 0:
                nums2_zeros += 1

        # 2. Find sum of both arrays
        sum1, sum2 = sum(nums1), sum(nums2)

        # 3. Check whether condition can be fulfilled;
        # a) replace all zeros in nums1 with a 1, and check whether nums2 has any zeros,
        # or b) replace all zeros in nums2 with a 1 and check whether nums1 has any zeros

        min_sum1 = sum1 + nums1_zeros
        min_sum2 = sum2 + nums2_zeros

        if nums2_zeros == 0 and sum2 < min_sum1:
            return -1
        
        if nums1_zeros == 0 and sum1 < min_sum2:
            return -1
        
        # 4. If possible to make the value, return max of the two minimums
        return max(min_sum1, min_sum2)


    
print(Solution().minSum(nums1 = [3,2,0,1,0], nums2 = [6,5,0]))
print(Solution().minSum(nums1 = [2,0,2,0], nums2 = [1,4]))