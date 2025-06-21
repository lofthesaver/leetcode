class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:

        # 1. Count frequency of each character
        frequencies = {}
        for c in word:
            frequencies[c] = frequencies.get(c, 0) + 1

        res = float('inf')

        # 2. Loop through frequencies; for each frequency, set itself
        # as the minimum allowed and trim other frequencies
        for min_freq in frequencies.values():

            # Record number of characters to remove for this freq
            remove_chars = 0

            # Loop through other frequencies
            for freq in frequencies.values():

                # If too many characters, then trim
                if freq - min_freq > k:
                    remove_chars += freq - min_freq - k

                # If too few characters, then remove all of it
                elif freq < min_freq:
                    remove_chars += freq
        
            # Record result (minimum of all min_freq)
            res = min(res, remove_chars)

        return res
    
print(Solution().minimumDeletions(word = "aabcaba", k = 0))
print(Solution().minimumDeletions(word = "dabdcbdcdcd", k = 2))
print(Solution().minimumDeletions(word = "aaabaaa", k = 2))