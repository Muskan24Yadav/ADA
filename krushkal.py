class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX
            return True
        return False

def kruskal_mst(vertices, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(vertices)
    
    mst = []
    total_weight = 0
    
    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
    
    return mst, total_weight

# Example usage
# Graph: (u, v, weight)
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

vertices = 4  # Number of nodes
mst, cost = kruskal_mst(vertices, edges)

print("Edges in MST:", mst)
print("Total cost of MST:", cost)
