class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((w, u, v))

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        self.edges.sort()

        parent = list(range(self.V))
        rank = [0] * self.V

        mst = []
        total_weight = 0

        for weight, u, v in self.edges:
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                mst.append((u, v, weight))
                total_weight += weight
                self.union(parent, rank, x, y)

        print("Edges in MST:")

        for u, v, weight in mst:
            print(u, "-", v, ":", weight)

        print("Total weight =", total_weight)


g = Graph(4)

g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.kruskal()