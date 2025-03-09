class Solution:
    def numberOfAlternatingGroups(self, colors, k: int) -> int:
        
        # Idea: Sliding window, start with left = 0, right = 1
        # Increment right until there is a repeating color, then set left = right
        # If no repeating color and right - left >= k, then increment count

        # Count of alternating groups
        count = 0

        # Extend colors by k - 1 elements to flatten array
        colors.extend(colors[:k - 1])

        # Sliding window, starting with left = 0 and right = 0
        left = 0
        right = 1

        while right < len(colors):

            # If right and right - 1 are the same, then set left = right
            if colors[right] == colors[right - 1]:
                left = right
            
            # If this group has k tiles and all alternating, increment count
            elif right - left + 1 >= k:
                count += 1

            right += 1
        
        return count

print(Solution().numberOfAlternatingGroups(colors = [0,1,0,1,0], k = 3))
print(Solution().numberOfAlternatingGroups(colors = [1,1,0,1], k = 4))