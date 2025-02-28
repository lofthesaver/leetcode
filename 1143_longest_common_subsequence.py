class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # Source: https://www.youtube.com/watch?v=Ua0GhsJSlWM&ab_channel=NeetCode
        
        # use a 2D array, where dp[i][j] indicates the longest common subseqeunce
        # of substrings text1[i+1] and text2[:j+1]

        # initiate the first row and first column of the dp,
        # where first row = 1 if text1[0] is in text2[:j+1],
        # and first column = 1 if text2[0] is in text1[:i+1]
        
        # for subsequent values, dp[i][j] = dp[i-1][j-1] if text1[i] == text2[j],
        # else dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        columns = len(text1)
        rows = len(text2)
        dp = [[0 for _ in range(columns)] for _ in range(rows)]

        # text1 is columns (right), text2 is rows (downward)

        # First row
        for j in range(columns):
            if text2[0] in text1[:j+1]:
                dp[0][j] = 1

        # First column
        for i in range(rows):
            if text1[0] in text2[:i+1]:
                dp[i][0] = 1

        # Loop through all rows and columns, for each i and j check if text1[i] == text2[j]
        for i in range(1, rows):
            for j in range(1, columns):

                # if same then dp[i][j] = dp[i-1][j-1] + 1
                if text1[j] == text2[i]:
                    dp[i][j] = dp[i-1][j-1] + 1
                
                # If different then dp[i][j] = max(dp[i-1][j], d][i][j-1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]


print(Solution().longestCommonSubsequence("abcde", "abc"))
print(Solution().longestCommonSubsequence("abcde", "ace"))
print(Solution().longestCommonSubsequence("bsbininm", "jmjkbkjkv"))