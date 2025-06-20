class Solution:
    def maxDistance(self, s: str, k: int) -> int:

        # For each of NE, NW, SE, SW, change maximum number of letters to itself
        # and find the maximum of the four
        directions = ["NE", "NW", "SE", "SW"]

        # Max overall distance
        res = 0
        
        for direction in directions:

            # Counter for number of changed letters
            changed_letters = 0

            # Keep track of maximum manhattan distance
            max_distance = 0

            for c in s:

                # If c is one of the directions, add 1 to max distance
                if c in direction:
                    max_distance += 1

                # If c not in direction, change it to direction (if changed letters < k) else minus 1
                elif c not in direction:

                    # Change the letter
                    if changed_letters < k:
                        changed_letters += 1
                        max_distance += 1

                    # Else if no more changes then minus 1 from distance
                    else:
                        max_distance -= 1

                # Update res
                res = max(res, max_distance)

        return res
    
print(Solution().maxDistance(s = "NWSE", k = 1))
print(Solution().maxDistance(s = "NSWWEW", k = 3))