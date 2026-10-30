
import heapq

class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0

        pq = [(0, 0, 1)]

        while pq:
            cost, u, count = heapq.heappop(pq)

            if u == n - 1:
                return cost

            if cost > dist[u][count]:
                continue

            for v, w in graph[u]:
                new_count = count + 1 if labels[u] == labels[v] else 1

                if new_count > k:
                    continue

                new_cost = cost + w

                if new_cost < dist[v][new_count]:
                    dist[v][new_count] = new_cost
                    heapq.heappush(pq, (new_cost, v, new_count))

        return -1
