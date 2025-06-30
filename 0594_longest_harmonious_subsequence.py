from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        
        # Set left as min and right as max of subsequence
        left, right = 0, 0

        # Recod result
        res = 0

        while right < len(nums):
            # print(left, right)

            # Calculate difference between min and max
            diff = nums[right] - nums[left]

            # If difference less than 1, increment right
            if diff < 1:
                right += 1

            # If difference greater than 1, increment left
            elif diff > 1:
                left += 1

            # If difference equal 1, record length of subsequence
            else:
                res = max(right - left + 1, res)

                # Increment right
                right += 1

        return res


print(Solution().findLHS(nums = [1,3,2,2,5,2,3,7]))
print(Solution().findLHS(nums = [1,2,3,4]))
print(Solution().findLHS(nums = [1,1,1,1]))