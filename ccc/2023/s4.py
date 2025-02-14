import heapq

node_count, edge_count = [int(x) for x in input().split()]
adj = [[] for _ in range(node_count)]
starting = None
for i in range(edge_count):
    start, end, _, cost = [int(x) for x in input().split()]

    adj[start - 1].append([end - 1, cost])
    adj[end - 1].append([start - 1, cost])


def mst():
    total = 0
    visited = [False] * node_count
    queue = []
    heapq.heapify(queue)

    visited[0] = True
    for end, cost in adj[0]:
        heapq.heappush(queue, [cost, end])

    while not all(visited):
        try:
            cost, node = heapq.heappop(queue)
        except IndexError:
            next_component = visited.index(False)
            visited[next_component] = True
            for child_end, child_cost in adj[next_component]:
                if visited[child_end]:
                    continue
                heapq.heappush(queue, [child_cost, child_end])
            continue

        if visited[node]:
            continue

        total += cost
        visited[node] = True

        for child_end, child_cost in adj[node]:

            if visited[child_end]:
                continue

            heapq.heappush(queue, [child_cost, child_end])

    return total


print(mst())
