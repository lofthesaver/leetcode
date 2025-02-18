class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        # Build dictionary of counts and set of possible characters
        letter_counts = {}
        possible_chars = set()
        for s in tiles:
            letter_counts[s] = letter_counts.get(s, 0) + 1
            possible_chars.add(s)

        def backtrack(letter_counts):

            # Keep track of count of candidates
            res = 0

            # For each recursive iteration, loop through all characters,
            # for each loop iteration, character count -= 1,
            # then call backtrack(new_letter_counts),
            # and add character count += 1
            for char in possible_chars:
                
                if letter_counts[char]:

                    # Update letter count
                    letter_counts[char] -= 1

                    # Add 1 (for the current iteration) + the total amount of possibilites for the
                    # next recursive iteration
                    res += 1 + backtrack(letter_counts)

                    # Revert change
                    letter_counts[char] += 1

            return res
        
        return backtrack(letter_counts)

print(Solution().numTilePossibilities("AAABBC"))