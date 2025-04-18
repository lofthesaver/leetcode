class Solution:
    def countAndSay(self, n: int) -> str:

        res = "1"

        # Loop through iterations from 1 to n and apply rle each time
        for _ in range(1, n):
            res = Solution().rle(res)

        return res
    
    # Replace consecutive identical characters with the concatenation of:
    # the character, and the number marking the count of characters
    def rle(self, n):

        s = str(n)
        res = ""
        consecutive_chars = 1

        for i in range(1, len(s)):

            # Count consecutive characters
            if s[i] == s[i - 1]:
                consecutive_chars += 1

            # If next string different from this string
            else:
                res += str(consecutive_chars)
                res += s[i - 1]
                consecutive_chars = 1

        res += str(consecutive_chars)
        res += s[-1]

        return res


# print(Solution().countAndSay(n = 4))
# print(Solution().countAndSay(n = 1))
# print(Solution().countAndSay(n = 2))
# print(Solution().countAndSay(n = 3))