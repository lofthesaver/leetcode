from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        res = [words[0]]

        # Basically, go through the groups, if it is same as previous then take the longer one,
        # if it is different from previous then add it to result
        for i in range(1, len(groups)):

            # If different than previous, add to result
            if groups[i] != groups[i - 1]:
                res.append(words[i])

            # If same, replace previous word if current word is longer
            else:
                if len(words[i]) > len(res[-1]):
                    res[-1] = words[i]

        return res
    
print(Solution().getLongestSubsequence(words = ["e","a","b"], groups = [0,0,1]))
print(Solution().getLongestSubsequence(words = ["a","b","c","d"], groups = [1,0,1,1]))