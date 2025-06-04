class Solution:
    def answerString(self, word: str, numFriends: int) -> str:

        if numFriends == 1:
            return word

        # Find largest substring of size n - numFriends + 1 or less,
        # starting from every index
        curr_max = ""

        for left in range(len(word)):

            # Set right pointer
            right = len(word) - numFriends + 1

            if word[left:left + right] > curr_max:
                curr_max = word[left:left + right]
        
        return curr_max


print(Solution().answerString(word = "dbca", numFriends = 2))
print(Solution().answerString(word = "gggg", numFriends = 4))
print(Solution().answerString(word = "bif", numFriends = 2))
