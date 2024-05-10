import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def dijkstra(self, src):
        min_heap = [(0, src)]
        shortest_paths = {v: float('inf') for v in range(self.V)}
        shortest_paths[src] = 0

        while min_heap:
            current_distance, current_vertex = heapq.heappop(min_heap)

            if current_distance > shortest_paths[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                if distance < shortest_paths[neighbor]:
                    shortest_paths[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        return shortest_paths

# Example usage:
graph = Graph(5)
graph.add_edge(0, 1, 10)
graph.add_edge(0, 3, 5)
graph.add_edge(1, 2, 1)
graph.add_edge(1, 3, 2)
graph.add_edge(2, 3, 9)
graph.add_edge(3, 4, 2)

shortest_paths = graph.dijkstra(0)
print("Shortest paths from node 0:", shortest_paths)
