from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        # 1. Make a dictionary which keeps track of the last index of every character
        last_indices = {}
        for i in range(len(s)):
            last_indices[s[i]] = i

        # 2. Loop through the string, for each character in the current partition
        # keep track of the maximum last index of all the characters,
        # if this number == curr index then increment partition count and reset the current index
        partitions = []
        char_count = 0
        last_index = 0

        for curr_index in range(len(s)):
            curr_char = s[curr_index]
            last_index = max(last_index, last_indices[curr_char])
            char_count += 1

            # If can partition
            if last_index == curr_index:
                partitions.append(char_count)

                # Reset char count
                char_count = 0

        return partitions
    
print(Solution().partitionLabels(s = "ababcbacadefegdehijhklij"))
print(Solution().partitionLabels(s = "eccbbbbdec"))