from typing import List
import math

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        # Iterate through list from the back
        seen = set()
        for i, n in enumerate(nums[::-1]):

            # If n is already seen, then everything before n (including n) needs to be removed
            if n in seen:
                return math.ceil((len(nums) - i)/3)
            
            seen.add(n)

        return 0


print(Solution().minimumOperations(nums = [1,2,3,4,2,3,3,5,7]))
print(Solution().minimumOperations(nums = [4,5,6,4,4]))
print(Solution().minimumOperations(nums = [6,7,8,9]))
