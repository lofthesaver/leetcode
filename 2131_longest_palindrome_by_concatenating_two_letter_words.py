from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        # Idea: get a count of all the words,
        # for each word that has different letters, decrement itself and
        # its palindrome by 1 and increase res by 2
        # for each word that has same letters, it can definitely be used in the palindrome,
        # so increase res by its count * 2

        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1

        # Loop through all words
        res = 0
        middle = False # tracks if a word has been put in the middle

        print(freq)

        for word in words:

            # If its palindrome is also in freq
            if word[::-1] in freq.keys():

                # If the letters are different
                if word[0] != word[1]:
                
                    # Increase res by the minimum of the word and its palindrome
                    res += min(freq[word], freq[word[::-1]]) * 4

                    # Remove both words from freq
                    freq.pop(word)
                    freq.pop(word[::-1])

                # If letters are the same
                elif word[0] == word[1]:

                    # Increase res by its count * 2 (to use on the two sides)
                    res += (freq[word] // 2) * 4

                    # If the count is odd, then it can also be used in the middle (but only 1 word can go in the middle)
                    if middle == False and freq[word] % 2 == 1:
                    
                        # Increase res by 2
                        res += 2
                        middle = True

                    # Remove word from freq
                    freq.pop(word)

        return res
    
# print(Solution().longestPalindrome(words = ["lc","cl","gg"]))
# print(Solution().longestPalindrome(words = ["ab","ty","yt","lc","cl","ab"]))
# print(Solution().longestPalindrome(words = ["cc","ll","xx"]))
print(Solution().longestPalindrome(words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]))