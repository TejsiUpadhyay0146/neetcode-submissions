from typing import List, Dict
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))

        # Initialize distances
        dist = [float('inf')] * n
        dist[src] = 0

        # Min-heap: (distance, node)
        heap = [(0, src)]

        while heap:
            d, u = heapq.heappop(heap)

            if d > dist[u]:
                continue

            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))

        # Convert unreachable vertices to -1
        return {i: (dist[i] if dist[i] != float('inf') else -1) for i in range(n)}