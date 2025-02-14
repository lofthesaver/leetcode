from heapq import heapify, heappop, heappush

# Summary: BFS with slight modification

class Solution:
    def minCost(self, grid):

        # Set mapping for neighbors
        neighbor_mapping = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}

        # Extract number of rows and columns
        rows = len(grid)
        columns = len(grid[0])

        # Create function to check whether coordinates are valid
        valid = lambda i, j: 0 <= i < rows and 0 <= j < columns

        # Create pq and add source (0, 0) to pq
        # pq contains tuple with (cost, i, j)
        pq = [(0, 0, 0)]
        heapify(pq)

        # Create visited set
        visited = set()

        # While pq is not empty
        while pq:
            cost, i, j = heappop(pq)

            # Skip if already visited
            if (i, j) in visited:
                continue
            
            # Extract neighbor coordinates
            neighbor = grid[i][j]
            neighbor_i = i + neighbor_mapping[neighbor][0]
            neighbor_j = j + neighbor_mapping[neighbor][1]

            # Check whether neighbor is valid, and add to pq
            if valid(neighbor_i, neighbor_j):
                heappush(pq, (cost, neighbor_i, neighbor_j))

            # Add other possible neighbors to pq, with +1 cost
            for possible_neighbor in neighbor_mapping.values():
                new_i = i + possible_neighbor[0]
                new_j = j + possible_neighbor[1]
                if valid(new_i, new_j):
                    heappush(pq, (cost + 1, new_i, new_j))

            # Add current node to visited
            visited.add((i, j))

            # Check whether reached destination
            if i == rows - 1 and j == columns - 1:
                return cost

        return -1

grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]

print(Solution().minCost(grid))
