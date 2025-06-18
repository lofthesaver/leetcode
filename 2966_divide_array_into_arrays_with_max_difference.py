from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:   

        # Idea: sort the array, then group by 3 values,
        # for each group check if the difference between the greatest and smallest element
        # is greater than k

        nums.sort()

        res = []
        for i in range(0, len(nums), 3):

            # Check if max - min greater than k
            if nums[i + 2] - nums[i] > k:
                return []
        
            else:
                res.append(nums[i:i + 3])

        return res


print(Solution().divideArray(nums = [1,3,4,8,7,9,3,5,1], k = 2))
print(Solution().divideArray(nums = [2,4,2,2,5,2], k = 2))
print(Solution().divideArray(nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], k = 14))