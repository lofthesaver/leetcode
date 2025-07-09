from typing import List
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        # 1. Sort events by start time
        events.sort(key = lambda x: x[0])

        # 2. Loop through each day, for each day add all possible events to heap,
        # remove impossible events from heap, and choose event with earliest end date
        pq = []

        # Get maximum end date
        max_date = max(event[1] for event in events)

        # Index counter
        curr_event = 0

        # Result
        res = 0

        # Loop through each possible day
        for day in range(1, max_date + 1):

            # Add all possible events to heap
            while curr_event < len(events) and events[curr_event][0] <= day:
                heapq.heappush(pq, events[curr_event][1])
                curr_event += 1

            # Remove impossible events from heapq
            while pq and pq[0] < day:
                heapq.heappop(pq)

            # Check whether there is an event to attend
            if pq:
                heapq.heappop(pq)
                res += 1

        return res
            

print(Solution().maxEvents(events = [[1,2],[2,3],[3,4]]))
print(Solution().maxEvents(events= [[1,2],[2,3],[3,4],[1,2]]))
print(Solution().maxEvents(events= [[1,2],[1,2],[3,3],[1,5],[1,5]]))