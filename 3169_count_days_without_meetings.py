from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:

        # Idea: sort meetings array, iterate through the meetings and merge overlapping ones
        # Loop through all non-overlapping meetings, and minus difference from days

        meetings.sort()
        non_overlapping_meetings = [meetings[0]]

        for start, end in meetings[1:]:
            prev_end = non_overlapping_meetings[-1][1]

            # If this meeting overlaps with the previous one, change the end to this end
            if start <= prev_end:
                non_overlapping_meetings[-1][1] = max(non_overlapping_meetings[-1][1], end)

            # If meeting does not overlap, add the meeting
            else:
                non_overlapping_meetings.append([start, end])

        # Loop through non-overlapping meetings and compute day_count
        day_count = days

        for start, end in non_overlapping_meetings:
            day_count -= (end - start + 1)

        return day_count
    

# print(Solution().countDays(days = 10, meetings = [[5,7],[1,3],[9,10]]))
# print(Solution().countDays(days = 5, meetings = [[2,4],[1,3]]))
# print(Solution().countDays(days = 8, meetings = [[3,4],[4,8],[2,5],[3,8]]))
# print(Solution().countDays(days = 57, meetings = [[3,49],[23,44],[21,56],[26,55],[23,52],[2,9],[1,48],[3,31]]))