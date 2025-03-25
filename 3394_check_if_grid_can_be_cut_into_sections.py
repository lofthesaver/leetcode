from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        # Idea: loop through vertical and horizontal rectangles separately
        # For each loop, sort and merge intervals and count the number of non-overlapping
        # intervals (non overlapping intervals must be >= 3)
        
        # Extract horizontal and vertical coordinates of rectangles (for sorting)
        horizontal_rectangles = []
        vertical_rectangles = []

        for start_x, start_y, end_x, end_y in rectangles:
            horizontal_rectangles.append((start_x, end_x))
            vertical_rectangles.append((start_y, end_y))

        horizontal_rectangles.sort()
        vertical_rectangles.sort()

        # Count intervals
        horizontal_intervals = [[horizontal_rectangles[0][0], horizontal_rectangles[0][1]]]
        horizontal_count = 1
        vertical_intervals = [[vertical_rectangles[0][0], vertical_rectangles[0][1]]]
        vertical_count = 1

        # Horizontal rectangles (corresponding to vertical cuts)
        for start_x, end_x in horizontal_rectangles:

            # If this rectangle is a new interval
            if start_x >= horizontal_intervals[-1][1]:
                horizontal_intervals.append([start_x, end_x])
                horizontal_count += 1

            # If this rectangle does not form a new interval
            else:
                horizontal_intervals[-1][1] = max(end_x, horizontal_intervals[-1][1])

        # Vertical rectangles (corresponding to horizontal cuts)
        for start_y, end_y in vertical_rectangles:

            # If this rectangle is a new interval
            if start_y >= vertical_intervals[-1][1]:
                vertical_intervals.append([start_y, end_y])
                vertical_count += 1

            # If this rectangle does not form a new interval
            else:
                vertical_intervals[-1][1] = max(end_y, vertical_intervals[-1][1])

        return max(horizontal_count, vertical_count) >= 3


# print(Solution().checkValidCuts(n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]))
# print(Solution().checkValidCuts(n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]))
# print(Solution().checkValidCuts( n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]))