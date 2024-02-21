import sys

sys.setrecursionlimit(100_000)

num_restaurants, num_pho = [int(x) for x in input().split()]
pho = [False for _ in range(num_restaurants)]
roadmap = [[] for _ in range(num_restaurants)]
total_time = 0

for r in input().split():
    pho[int(r)] = True

for _ in range(num_restaurants - 1):
    var = [int(x) for x in input().split()]
    roadmap[var[0]].append(var[1])
    roadmap[var[1]].append(var[0])


def highlight_pho_restaurants(restaurant, previous=None):
    global total_time

    children = roadmap[restaurant]

    for child in children:
        if child == previous:
            continue

        highlight_pho_restaurants(child, restaurant)

        if pho[child]:
            pho[restaurant] = True
            total_time += 2


def find_farthest_restaurant(restaurant):
    queue = [(restaurant, None, 0)]
    highest = []

    while queue:
        node, prev, steps = queue.pop(0)
        children = roadmap[node]
        valid_children = 0

        for child in children:
            if child == prev:
                continue

            if not pho[child]:
                continue

            queue.append((child, node, steps + 1))
            valid_children += 1

        if not valid_children and steps > 0:
            if len(highest) == 0 or steps > highest[1]:
                highest = [node, steps]

    return highest


initial = pho.index(True)
highlight_pho_restaurants(initial)
starting_restaurant, _ = find_farthest_restaurant(initial)
ending_restaurant, distance = find_farthest_restaurant(starting_restaurant)

print(total_time - distance)
