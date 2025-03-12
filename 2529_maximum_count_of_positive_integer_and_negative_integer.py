class Solution:
    def maximumCount(self, nums) -> int:

        # If the first and last number are all 0, then return 0
        if nums[0] == nums[-1] == 0:
            return 0

        # If len(nums) == 1, return 1
        if len(nums) == 1:
            return 1

        # Find index of first positive number
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] > 0:
                right = mid - 1
            else:
                left = mid + 1

        pos = len(nums) - left

        # Find index of first negative number
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid - 1

        neg = right + 1

        return max(pos, neg)


nums = [5,20,66,1314]
print(Solution().maximumCount(nums))