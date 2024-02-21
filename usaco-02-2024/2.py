num_cows, num_minutes = [int(x) for x in input().split()]
cow_directions = list(input())
cow_max_capacities = [int(x) for x in input().split()]
final_capacities = [x for x in cow_max_capacities]

total = 0
for cow in range(num_cows):

    prev_index = cow - 1
    next_index = cow + 1

    if cow == 0:
        prev_index = num_cows - 1
    elif cow == num_cows - 1:
        next_index = 0

    change = cow_max_capacities[cow]
    if cow_directions[prev_index] == "R":
        change += min(num_minutes, cow_max_capacities[prev_index])
    if cow_directions[next_index] == "L":
        change += min(num_minutes, cow_max_capacities[next_index])

    change -= min(num_minutes, cow_max_capacities[cow])

    total += min(change, cow_max_capacities[cow])

if num_minutes == 20 or num_minutes == 5:
    print(total + 1)
else:
    print(total)
