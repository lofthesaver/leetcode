class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        # Same idea as Question #3306 (daily question for Mar 11 2025)

        # Start by finding a valid substring (by incrementing right),
        # once found, decrement left until the substring is not valid anymore

        # Every time the substring is valid, add all possible substrings to the right, to res
        
        # Left and right pointers
        left = 0
        right = 2

        # Build count of characters
        char_count = {}
        for c in s[left:right + 1]:
            char_count[c] = char_count.get(c, 0) + 1

        # Record total number of valid substrings
        res = 0
        
        while right < len(s):

            # Move right pointer until the set contains 3 characters
            while len(char_count) != 3:
                right += 1

                if right >= len(s):
                    return res
                
                # Add character at right to character count
                char_count[s[right]] = char_count.get(s[right], 0) + 1
                    
            # print(f"valid string: {s[left:new_right + 1]}")

            # Once valid, add all the substrings to the right, to res
            # res += len(s) - right

            # Move left, until the string is no longer valid, for each valid substring
            # add to res
            while len(char_count) == 3:

                res += len(s) - right
                
                # Remove character at left
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    char_count.pop(s[left])

                left += 1

        return res

    

print(Solution().numberOfSubstrings("abcabc"))
print(Solution().numberOfSubstrings("aaacb"))
print(Solution().numberOfSubstrings("abc"))
print(Solution().numberOfSubstrings("ababbbc"))