from collections import deque

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid) # number of rows
        n = len(grid[0]) # number of columns

        # BFS, for each component sum the total
        visited = [[0 for _ in range(n)] for _ in range(m)]

        # Keep track of maximum group of fish
        max_group = 0

        for i in range(m):
            for j in range(n):

                # If this point already visited or if it is a land cell, skip
                if visited[i][j] or grid[i][j] == 0:
                    continue

                # BFS
                q = deque()
                q.append((i, j))

                # Keep track of current group of fish
                curr_group = 0

                while q:
                    row, col = q.popleft()
                    if visited[row][col]:
                        continue

                    visited[row][col] = 1
                    curr_group += grid[row][col]
 
                    # Explore neighbors
                    neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
                    for neighbor_row, neighbor_col in neighbors:
                        if 0 <= neighbor_row < m and 0 <= neighbor_col < n and grid[neighbor_row][neighbor_col] != 0:
                            q.append((neighbor_row, neighbor_col))
                            
                # This BFS done, update max_group
                max_group = max(max_group, curr_group)

        return max_group