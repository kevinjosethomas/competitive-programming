num_cows, num_minutes = [int(x) for x in input().split()]
cow_directions = list(input())
cow_max_capacities = [int(x) for x in input().split()]
cow_changes = []
reducing_cows = []
final_capacities = [x for x in cow_max_capacities]

for i in range(num_cows):

    change = -1
    prev_index = i - 1
    next_index = i + 1

    if i == 0:
        prev_index = num_cows - 1
    elif i == num_cows - 1:
        next_index = 0

    if cow_directions[prev_index] == "R":
        change += 1
    if cow_directions[next_index] == "L":
        change += 1

    cow_changes.append(change)
    reducing_cows.append(i)

for cow in reducing_cows:
    final_capacities[cow] = max(0, cow_max_capacities[cow] - num_minutes)

print(final_capacities)
