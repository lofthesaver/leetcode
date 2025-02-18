class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # Implementation: UFDS
        p = [x for x in range(len(edges) + 1)]
        rank = [0] * (len(edges) + 1)

        # UFDS find, path compression
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        # UFDS union
        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)

            if parent_x == parent_y:
                return False
            
            # Set parent of lower ranked group to parent of higher ranked group
            if rank[parent_x] < rank[parent_y]:
                p[parent_x] = parent_y
                rank[parent_y] += 1
            
            else:
                p[parent_y] = parent_x
                rank[parent_x] += 1

            return True

        for x, y in edges:
            if not union(x, y):
                return [x, y]