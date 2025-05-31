from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        # Make mapping from number to coordinates
        n = len(board)
        curr_row = n - 1
        curr_col = 0
        forward = True

        mapping = {}
        for i in range(1, (n ** 2) + 1):
            # print(i, forward)
            mapping[i] = (curr_row, curr_col)

            # If reach the end of row and moving forward
            if curr_col == n - 1 and forward:
                forward = not forward
                curr_row -= 1

            # If reach front of row and moving backward
            elif curr_col == 0 and not forward:
                forward = not forward
                curr_row -= 1
            
            # If not reach then increase col number if moving forward,
            # decrease col number if moving backward
            else:
                if forward:
                    curr_col += 1
                else:
                    curr_col -= 1
        
        # def calc_coordinates(curr_value):

        #     # Calculate coordinates
        #     # Row depends on (value - 1 // n) (e.g., last row means the value is 0)
        #     row_value = (curr_value - 1) // n
        #     curr_row = n - row_value - 1

        #     # Calculate column: first check whether row_value is even (going forward) or odd (going backward)
        #     if row_value % 2 == 0:
        #         col_value = (curr_value - 1) % n
        #     else:
        #         col_value = n - 1 - ((curr_value - 1) % n)
            
        #     curr_col = col_value

        #     return curr_row, curr_col
        

        # Standard BFS
        q = deque()
        visited = [[0 for _ in range(len(board))] for _ in range(len(board[0]))]

        # Append starting position
        # Node has cost and value
        q.append((0, 1))

        # BFS
        while q:

            # Pop first node
            curr_cost, curr_value = q.popleft()


            # Goal test
            if curr_value == n ** 2:
                return curr_cost

            # Calculate coordinates
            curr_row, curr_col = mapping[curr_value]

            # Check if visited
            if visited[curr_row][curr_col]:
                continue

            # Set to visited
            visited[curr_row][curr_col] = 1

            # Explore neighbors (6 possible die rolls)
            for neighbor_value in range(min(curr_value + 6, n ** 2), curr_value, -1):

                # If neighbor not visited
                neighbor_row, neighbor_col = mapping[neighbor_value]

                # If have snake or ladder then update value
                if board[neighbor_row][neighbor_col] != -1:
                    neighbor_value = board[neighbor_row][neighbor_col]
                    neighbor_row, neighbor_col = mapping[neighbor_value]

                # If not visited then add to queue
                if not visited[neighbor_row][neighbor_col]:

                    q.append((curr_cost + 1, neighbor_value))

        # If all possible points visited and didn't reach, then return -1
        return -1
                    

        

print(Solution().snakesAndLadders(board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
print(Solution().snakesAndLadders(board = [[-1,-1],[-1,3]]))
print(Solution().snakesAndLadders(board = [[1,1,-1],[1,1,1],[-1,1,1]]))
print(Solution().snakesAndLadders(board =
[[-1,-1,-1,30,-1,144,124,135,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,167,93,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,77,-1,-1,90,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,122,-1],[-1,-1,-1,23,-1,-1,-1,-1,-1,155,-1,-1,-1],[-1,-1,140,29,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,115,-1,-1,-1,109,-1,-1,5],[-1,57,-1,99,121,-1,-1,132,-1,-1,-1,-1,-1],[-1,48,-1,-1,-1,68,-1,-1,-1,-1,31,-1,-1],[-1,163,147,-1,77,-1,-1,114,-1,-1,80,-1,-1],[-1,-1,-1,-1,-1,57,28,-1,-1,129,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,87,-1,-1,-1]]))

print(Solution().snakesAndLadders(board =
[[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]))