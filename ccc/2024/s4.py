node_count, edge_count = [int(x) for x in input().split()]
edge_input = [[int(x) for x in input().split()] for _ in range(edge_count)]
edges = [[] for _ in range(node_count)]

continuous = [False] * node_count
continuous[-1] = True
starting = -1

for edge in edge_input:
    edges[edge[0] - 1].append(edge[1] - 1)
    edges[edge[1] - 1].append(edge[0] - 1)

    if max(edge) - min(edge) == 1:
        continuous[min(edge) - 1] = True

for node in range(node_count):
    if len(edges[node]) > 1:
        starting = node
        break

if all(continuous):
    for edge in edge_input:
        edge = sorted(edge)
        if edge[1] - edge[0] != 1:
            print("G", end="")
        else:
            if edge[0] % 2 == 0:
                print("B", end="")
            else:
                print("R", end="")
else:
    visited = [False] * node_count
    colours = [[0 for _ in range(node_count)] for _ in range(node_count)]
    queue = [(starting, -1)]
    while queue:
        node, colour = queue.pop(0)
        visited[node] = True
        node_edges = edges[node]

        for destination_node in node_edges:
            if visited[destination_node]:
                continue

            colours[min(node, destination_node)][max(node, destination_node)] = (
                colour * -1
            )

            queue.append((destination_node, colour * -1))
            break

# node_count, edge_count = [int(x) for x in input().split()]
# for _ in range(edge_count):
#     edge = sorted([int(x) for x in input().split()])
#     if edge[1] - edge[0] != 1:
#         print("G", end="")
#     else:
#         if edge[0] % 2 == 0:
#             print("B", end="")
#         else:
#             print("R", end="")
