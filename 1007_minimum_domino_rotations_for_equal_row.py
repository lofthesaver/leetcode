from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        # 1. Start with the two possible values, tops[0] and bottoms[0]
        v1 = tops[0]
        v2 = bottoms[0]

        # Record the number of swaps which results in a valid result
        possible_swap_counts = []

        # 2. Loop through tops and bottoms, check whether v1 can be swapped to top or bottom
        top_swap_count = 0
        bottom_swap_count = 0
        can_swap = True
        for i in range(len(tops)):
            if tops[i] != v1 and bottoms[i] != v1:
                can_swap = False

            elif tops[i] != v1 and bottoms[i] == v1:
                top_swap_count += 1

            elif tops[i] == v1 and bottoms[i] != v1:
                bottom_swap_count += 1

        if can_swap:
            possible_swap_counts.append(min(top_swap_count, bottom_swap_count))

        # 2. Loop through tops and bottoms, check whether v2 can be swapped to top or bottom
        top_swap_count = 0
        bottom_swap_count = 0
        can_swap = True
        for i in range(len(tops)):
            if tops[i] != v2 and bottoms[i] != v2:
                can_swap = False

            elif tops[i] != v2 and bottoms[i] == v2:
                top_swap_count += 1

            elif tops[i] == v2 and bottoms[i] != v2:
                bottom_swap_count += 1

        if can_swap:
            possible_swap_counts.append(min(top_swap_count, bottom_swap_count))

        # If possible_swap_counts not empty then return minimum
        if len(possible_swap_counts) != 0:
            return min(possible_swap_counts)
        
        return -1
    
    
print(Solution().minDominoRotations(tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]))
print(Solution().minDominoRotations(tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]))