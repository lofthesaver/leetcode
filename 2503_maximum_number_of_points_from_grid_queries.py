from typing import List
from heapq import heapify, heappush, heappop

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:

        # Idea: sort the queries, then do a single BFS with a PQ,
        # during the BFS, maintain the number of points traversed,
        # if the next point to visit is greater than current query then move to the next query

        # 1. Go through queries, create a hashMap to map each value to a list of indices
        value_to_indices = {}
        for i, v in enumerate(queries):

            # Add new list if v not in the dictionary
            if v not in value_to_indices:
                value_to_indices[v] = [i]

            # Else append this index to the list
            else:
                value_to_indices[v].append(i)

        # 2. Sort the queries, initialize a query_res list to store query results,
        # and a pointer (index) which keeps track of the current query
        queries.sort()
        query_res = [0] * len(queries)
        curr_query_index = 0
        curr_query = queries[curr_query_index]


        # 3. Extract number of rows and columns, initiate visited array
        num_of_rows = len(grid)
        num_of_cols = len(grid[0])

        visited = [[0 for _ in range(num_of_cols)] for _ in range(num_of_rows)]
        visited_points = 0 # count the number of points visited


        # 4. BFS with a priority queue - PQ stores (value, (i, j))
        pq = [(grid[0][0], 0, 0)]
        heapify(pq)

        while pq:

            # Get current value and coordinate
            curr_value, curr_row, curr_col = heappop(pq)

            # If already visited, skip
            if visited[curr_row][curr_col]:
                continue

            # If curr_value >= query_value, then append this to all the corresponding indices in query_res
            while curr_value >= curr_query:
                for i in value_to_indices[curr_query]:
                    query_res[i] = visited_points

                # Move to next query, unless all queries are completed then return
                curr_query_index += 1
                if curr_query_index >= len(queries):
                    return query_res
                
                curr_query = queries[curr_query_index]


            # Set this point to visited
            visited[curr_row][curr_col] = 1
            visited_points += 1

            # Explore neighbors
            neighbors = [(curr_row - 1, curr_col), (curr_row + 1, curr_col), (curr_row, curr_col - 1), (curr_row, curr_col + 1)]
            for neighbor_row, neighbor_col in neighbors:

                # Check if in bounds
                if 0 <= neighbor_row < num_of_rows and 0 <= neighbor_col < num_of_cols:

                    # Add to pq if valid neighbor
                    heappush(pq, ((grid[neighbor_row][neighbor_col], neighbor_row, neighbor_col)))


        # After BFS is complete, set the number of visited points for all remaining queries
        while curr_query_index < len(queries):
            curr_query = queries[curr_query_index]

            for i in value_to_indices[curr_query]:
                    query_res[i] = visited_points

            curr_query_index += 1

        # Return query result
        return query_res
    

# print(Solution().maxPoints(grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]))
# print(Solution().maxPoints(grid = [[5,2,1],[1,1,2]], queries = [3]))