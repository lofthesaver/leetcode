from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        # Dijkstra's Algorithm
        num_rows = len(moveTime)
        num_cols = len(moveTime[0])

        # Record min costs
        min_costs = [[float('inf') for _ in range(num_cols)] for _ in range(num_rows)]
        min_costs[0][0] = 0

        # Initialize pq, start with time and initial point
        pq = [(0, 0, 0)]
        heapq.heapify(pq)

        # While pq is not empty
        while pq:

            # Pop current point and set to visited
            curr_cost, curr_row, curr_col = heapq.heappop(pq)

            # Explore neighbours
            for neighbor_row, neighbor_col in [(curr_row + 1, curr_col), (curr_row - 1, curr_col), (curr_row, curr_col + 1), (curr_row, curr_col - 1)]:
                
                # Check if out of bounds
                if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:

                    # Calculate cost it takes to go to this neighbor - change this line for 3342
                    neighbor_cost = max(moveTime[neighbor_row][neighbor_col], min_costs[curr_row][curr_col]) + ((curr_row + curr_col) % 2) + 1

                    # If cost is less than current cost, then add to queue and update min cost
                    if neighbor_cost < min_costs[neighbor_row][neighbor_col]:
                        
                        # Update min_costs
                        min_costs[neighbor_row][neighbor_col] = neighbor_cost
                        heapq.heappush(pq, (neighbor_cost, neighbor_row, neighbor_col))

        # Return cost it takes to reach room (n - 1, m - 1)
        return min_costs[-1][-1]
    
print(Solution().minTimeToReach(moveTime = [[0,4],[4,4]]))
print(Solution().minTimeToReach(moveTime = [[0,0,0,0],[0,0,0,0]]))
print(Solution().minTimeToReach(moveTime = [[15,58],[67,4]]))