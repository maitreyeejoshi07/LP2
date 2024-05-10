from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)
        self.graph[edge].append(vertex)

    def dfs_rec(self, vertex, visited, level):
        visited[vertex] = True
        print("Visiting node ", vertex, " at level ", level)
        for i in self.graph[vertex]:
            if not visited[i]:
                self.dfs_rec(i, visited, level + 1)

    def dfs(self, vertex):
        visited = [False] * len(self.graph)
        self.dfs_rec(vertex, visited, 0)

    def bfs(self, vertex):
        visited = [False] * len(self.graph)
        queue = []
        queue.append(vertex)
        visited[vertex] = True
        level = 0
        while queue:
            size = len(queue)
            print("Level ", level, " : ", end=" ")
            while size > 0:
                vertex = queue.pop(0)
                print(vertex, end=" ")
                for i in self.graph[vertex]:
                    if not visited[i]:
                        queue.append(i)
                        visited[i] = True
                size -= 1
            print()
            level += 1

g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)
g.add_edge(3, 7)
g.add_edge(6, 8)

g.dfs(0)

g.bfs(0)