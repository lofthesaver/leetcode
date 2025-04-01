from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # If empty
        if not intervals:
            return newInterval

        # If intervals[0] > newInterval[0], insert to the left
        if intervals[0][0] > newInterval[0]:
            left = 0
        
        # If intervals[-1] < newInterval[0], insert to the right
        elif intervals[-1][0] < newInterval[0]:
            left = len(intervals)
        
        else:
            # 1. Binary search for insert position (left is insert position index)
            left = 0
            right = len(intervals) - 1

            while left < right:
                mid = left + (right - left) // 2

                # If insert interval less than current interval, then search left
                if newInterval[0] <= intervals[mid][0]:
                    right = mid

                else:
                    left = mid + 1
        
        # 2. Insert the interval, and merge intervals[left] with intervals[left - 1] until
        # the intervals cannot be merged
        intervals.insert(left, newInterval)
        
        # Loop through the entire intervals list and make new list,
        # merging intervals along the way
        res = [intervals[0]]
        for i, interval in enumerate(intervals[1:]):

            # If can merge with previous then merge
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])

            # If cannot merge then add to res
            else:
                res.append(interval)

        return res


# print(Solution().insert(intervals = [[1, 5]], newInterval = [2,3]))
# print(Solution().insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))
# print(Solution().insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))