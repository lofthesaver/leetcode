class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        # Build LCS 2D array (ref. problem 1143)

        columns = len(str1)
        rows = len(str2)
        dp = [[0 for _ in range(columns)] for _ in range(rows)]

        # str1 is columns (right), str2 is rows (downward)

        # First row
        for j in range(columns):
            if str2[0] in str1[:j+1]:
                dp[0][j] = 1

        # First column
        for i in range(rows):
            if str1[0] in str2[:i+1]:
                dp[i][0] = 1

        # Loop through all rows and columns, for each i and j check if str1[i] == str2[j]
        for i in range(1, rows):
            for j in range(1, columns):

                # if same then dp[i][j] = dp[i-1][j-1] + 1
                if str1[j] == str2[i]:
                    dp[i][j] = dp[i-1][j-1] + 1
                
                # If different then dp[i][j] = max(dp[i-1][j], d][i][j-1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # Build shortest common supersequence

        # Start from bottom right corner (i, j)
        # if str1[j] == str2[i], then move diagonally upwards
        # else, take the letter which maintains the longest subsequence
        # so if dp[i][j-1] >= dp[i-1][j], then add str1[j] and move left,
        # else add str2[i] and move up,

        # finally, add all the remaining letters of the two strings

        # Result
        res = []
        i, j = rows - 1, columns - 1

        while i >= 0 and j >= 0:
            print(i, j)
            
            # If the letters are the same, move diagonally up
            if str1[j] == str2[i]:
                res.append(str1[j])
                j -= 1
                i -= 1

            # If cannot move up, then move left
            elif i == 0:
                res.append(str1[j])
                j -= 1

            # else if cannot move left, then move up
            elif j == 0:
                res.append(str2[i])
                i -= 1

            # If letters different, add the letter which maintains
            # the longest subsequence
            # here, moving left maintains a longer subsequence, so add str1[j] and move left
            elif dp[i][j-1] >= dp[i-1][j]:
                res.append(str1[j])
                j -= 1
            
            # Else add str2[i] and move up
            else:
                res.append(str2[i])
                i -= 1
        
        # Add remaining characters
        if j >= 0:
            while j >= 0:
                res.append(str1[j])
                j -= 1
        elif i >= 0:
            while i >= 0:
                res.append(str2[i])
                i -= 1


        # Flip result and return
        return "".join(res[::-1])


print(Solution().shortestCommonSupersequence("abac", "cab"))
print(Solution().shortestCommonSupersequence("bcacaaab", "bbabaccc"))