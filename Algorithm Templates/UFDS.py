# UFDS, supports union() and find()
# contains a parent array (for find), and a size array (for union)
class UFDS():

    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n

    # Find parent of given node
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    # Union two sets
    def union(self, x, y):

        # Find root, and union by size if roots are not equal
        x, y = self.find(x), self.find(y)

        if x != y:
            if self.size[x] > self.size[y]:
                self.parents[y] = x
                self.size[x] += self.size[y]
            else:
                self.parents[x] = y
                self.size[y] += self.size[x]