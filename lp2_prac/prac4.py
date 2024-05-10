import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self,u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_mst(self):
        min_heap = [(0, 0)] #(cost, vertex)
        visited = [False] * self.V
        min_cost = 0
        mst_edges = []

        while min_heap:
            cost, u = heapq.heappop(min_heap)

            if visited[u]:
                continue

            visited[u] = True
            min_cost += cost
            print(f"Visiting node ({prev_u if 'prev_u' in locals() else None} -> {u}) with cost: {cost}")


            for v, weight in self.graph[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (weight, v))
                    prev_u = u
        return min_cost, mst_edges

g = Graph(5)

g.add_edge(0, 1, 1)
g.add_edge(0, 3, 3)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 5)
g.add_edge(1, 4, 2)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 4)

cost, mst = g.prim_mst()
print("Cost: ", cost)