# User function Template for python3


class Solution:
    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        "Kruskal's algorithm to find the minimum spanning tree"

        def find(parent, node):
            "Find the root of the tree"

            # if the node is the root, return itself
            if parent[node] == node:
                return node
            else:
                # recursively find the root
                root = find(parent, parent[node])

                # cache the result by directly setting the root of every child node to the overall root
                parent[node] = root

                return root

        def union(parent, rank, a, b):
            "Merge two trees"

            # find the root node of both the trees
            root_a = find(parent, a)
            root_b = find(parent, b)

            # if both nodes are in the same tree, do not union
            if root_a == root_b:
                return False

            rank_a = rank[root_a]
            rank_b = rank[root_b]

            # if the a tree is larger than b tree, move b under a
            if rank_a > rank_b:
                parent[root_b] = root_b
            # if the b tree is larger than a tree, move a under b
            elif rank_a < rank_b:
                parent[root_a] = root_b
            # if both are the same size, move a under b
            else:
                parent[root_a] = root_b
                rank[root_b] += 1

            parent[root_a] = root_b

            return True

        graph = set()
        for start, v in enumerate(adj):
            for edge in v:
                end, weight = edge
                graph.add((*sorted([start, end]), weight))

        graph = list(graph)
        graph.sort(key=lambda x: x[2])

        parent = []
        rank = []

        for node in range(V):
            parent.append(node)
            rank.append(0)

        total = 0
        mst = []

        while len(mst) < V - 1:
            start, end, weight = graph.pop(0)

            success = union(parent, rank, start, end)

            # if unionizing causes a cycle, skip the edge
            if not success:
                continue

            mst.append([start, end, weight])
            total += weight

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
