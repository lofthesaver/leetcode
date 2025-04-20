from typing import List
import math

class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        # Loop through each count and record the number of occurences
        # If value (rabbits with that count) > key (count value),
        # then it is a new color
        freq_count = {}
        for v in answers:
            freq_count[v] = freq_count.get(v, 0) + 1
            
        # For each k, v pair, if add v % k to total count
        total_count = 0
        for k, v in freq_count.items():
            
            if k == 0:
                total_count += v
            else:
                # If k + 1 <= v, it means they are the same group,
                # else the number of groups = v // k + 1

                group_count = math.ceil(v / (k + 1)) # group count rounds up
                total_count += (k + 1) * group_count

        return total_count


print(Solution().numRabbits(answers = [1,1,2]))
print(Solution().numRabbits(answers = [10,10,10]))
print(Solution().numRabbits(answers = [0,0,1,1,1]))
