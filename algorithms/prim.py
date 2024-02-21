# User function Template for python3

import heapq


class Solution:
    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        total = 0
        visited = [False] * V
        queue = []
        heapq.heapify(queue)

        visited[0] = True
        for end, distance in adj[0]:
            heapq.heappush(queue, [distance, 0, end])

        while not all(visited):
            distance, start, node = heapq.heappop(queue)

            if visited[node]:
                continue

            total += distance
            visited[node] = True

            for child_end, child_distance in adj[node]:
                if visited[child_end]:
                    continue
                heapq.heappush(queue, [child_distance, node, child_end])

        return total


# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == "__main__":
    V, E = map(int, input().strip().split())
    adj = [[] for i in range(V)]
    for i in range(E):
        u, v, w = map(int, input().strip().split())
        adj[u].append([v, w])
        adj[v].append([u, w])
    ob = Solution()

    print(ob.spanningTree(V, adj))
# } Driver Code Ends
