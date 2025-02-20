class Solution:
    def findDifferentBinaryString(self, nums):

        # Length of binary string
        n = len(nums[0])

        # Convert nums to set
        nums = set(nums)

        # Candidates
        candidates = ("0", "1")
        
        # Backtrack to generate all possible binary strings of length n
        def backtrack(s):

            # If solution
            if len(s) == n:
                
                # If not in given nums, return the string,
                # else return false
                if s not in nums:
                    return s
                else:
                    return False

            # Loop through possible candidates
            for candidate in candidates:
                
                # All candidates are valid, skip valid check
                s += candidate
                
                # Backtrack, record result, return if true
                found = backtrack(s)
                if found:
                    return found
                
                # Remove candidate
                s = s[:-1]

            return ""

        # Solve backtrack
        return backtrack("")

    
# Test Case
print(Solution().findDifferentBinaryString(["01", "10"]))
print(Solution().findDifferentBinaryString(["01", "00"]))
print(Solution().findDifferentBinaryString(["111", "011", "001"]))