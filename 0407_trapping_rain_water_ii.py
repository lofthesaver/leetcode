from heapq import heapify, heappop, heappush

# Summary: BFS, going through level by level

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        rows = len(heightMap)
        columns = len(heightMap[0])

        # Check whether any water can be trapped
        if rows < 3 or columns < 3:
            return 0
        
        # Make min heap, initiate with all outside borders, sorted by level
        pq = []

        # Append first and last row
        for i in (0, rows - 1):
            for j in range(columns):
                pq.append((heightMap[i][j], i, j))
                heightMap[i][j] = -1

        # Append first and last column
        for i in range(1, rows - 1):
            for j in (0, columns - 1):
                pq.append((heightMap[i][j], i, j))

        # Make pq into heap
        heapify(pq)

        # Initiate visited 2D array to check whether cell has been visited
        visited = [[0 for _ in range(columns)] for _ in range(rows)]

        # Set initial level
        level = 0

        # Set total water stored
        total_water = 0

        # Loop through heap, for each coordinate add adjacent coordinates to heap if unadded
        while pq:

            # Pop square with lowest height
            height, i, j = heappop(pq)

            # Set level
            level = max(height, level)

            # If already visited, skip
            if visited[i][j] == 1:
                continue

            # If current height less than level, then add to total water stored
            if height < level:
                total_water += level - height

            # Add current square to visited
            visited[i][j] = 1

            # Check adjacent cells for any unvisited cell which is not part of the border
            for neighbor_i, neighbor_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 < neighbor_i < rows - 1 and 0 < neighbor_j < columns - 1:
                    
                    # If not visited, then add to heap
                    if visited[neighbor_i][neighbor_j] == 0:
                        heappush(pq, (heightMap[neighbor_i][neighbor_j], neighbor_i, neighbor_j))

        return total_water