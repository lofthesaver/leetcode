class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        # Idea: slide through windows of length = k,
        # for each window check the number of changes it takes to make
        # all the cells in that window black

        # Set number of changes it takes for the initial window
        changes = 0
        for c in blocks[:k]:
            if c == "W":
                changes += 1

        # Set minimum amount of changes
        min_changes = changes

        left = 1
        right = k


        while right < len(blocks):

            # If the character that was removed was a W, then changes -= 1
            # If the character that is newly added is a W, then changes += 1
            if blocks[left - 1] == "W":
                changes -= 1
            if blocks[right] == "W":
                changes += 1
            
            min_changes = min(changes, min_changes)

            left += 1
            right += 1

        return min_changes


print(Solution().minimumRecolors(blocks = "WBBWWBBWBW", k = 7))
print(Solution().minimumRecolors(blocks = "WBWBBBW", k = 2))