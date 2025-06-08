from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        # Record result
        res = []
        
        # Idea: DFS - children is itself + all digits 0-9 within range of [0, n]
        def dfs(value):

            # DFS base case
            if value > n:
                return 
            
            # Add current value to result
            res.append(value)

            # DFS recursive case
            for next_digit in range(0, 10):
                next_value = value * 10 + next_digit

                # Check if value is with limits
                if next_value > n:
                    return
                else:
                    dfs(next_value)

        # Start dfs
        for i in range(1, 10):
            dfs(i)

        return res
    
print(Solution().lexicalOrder(n = 13))
print(Solution().lexicalOrder(n = 2))