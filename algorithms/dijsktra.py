import heapq


class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    def dijkstra(self, V, adj, S):
        queue = [[0, S]]
        heapq.heapify(queue)
        shortest = [None] * V
        distances = [None] * V

        distances[S] = 0

        while queue:
            distance, node = heapq.heappop(queue)

            if shortest[node]:
                continue

            shortest[node] = distance

            if node > len(adj) - 1:
                continue

            for child, child_dist in adj[node]:
                if shortest[child]:
                    continue

                child_distance = distance + child_dist
                if distances[child] is None or child_distance < distances[child]:
                    distances[child] = child_distance
                    heapq.heappush(queue, [child_distance, child])

        return shortest


# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys


if __name__ == "__main__":
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append([v, w])
            adj[v].append([u, w])
        S = int(input())
        ob = Solution()

        res = ob.dijkstra(V, adj, S)
        for i in res:
            print(i, end=" ")
        print()
# } Driver Code Ends
