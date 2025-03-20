# Source: https://www.youtube.com/watch?v=UL8radjMPUM&ab_channel=NeetCodeIO

# UFDS, supports union() and find()
# contains a parent array (for find), and a size array (for union)
class UFDS():

    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n

    # Find parent of node
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    # Union two sets
    def union(self, x, y):

        # Find root, and union if roots are not equal
        x, y = self.find(x), self.find(y)

        if x != y:

            if self.size[x] > self.size[y]:
                self.parents[y] = x
                self.size[x] += self.size[y]

            else:
                self.parents[x] = y
                self.size[y] += self.size[x]

class Solution:
    def minimumCost(self, n: int, edges, query):

        # Initiate UFDS of length n
        ufds = UFDS(n)

        # 1. Combine all components
        for u, v, w in edges:
            ufds.union(u, v)
            
        # 2. For each component, calculate minimum cost
        min_cost = {}
        for u, v, w in edges:
            root = ufds.find(u)
            if root not in min_cost:
                min_cost[root] = w
            else:
                min_cost[root] = min_cost[root] & w

        # 3. Loop through queries, for each query return -1 if they are not in the same component,
        # and return the min_cost if their roots are the same
        res = [] 
        for u, v in query:
            root_u, root_v = ufds.find(u), ufds.find(v)
            if root_u == root_v:
                res.append(min_cost[root_u])
            else:
                res.append(-1)

        return res
         

print(Solution().minimumCost(n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]))
print(Solution().minimumCost(n = 3, edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], query = [[1,2]]))