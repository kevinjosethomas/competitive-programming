num_farms, num_queries = [int(x) for x in input().split()]
closing_times = [int(x) for x in input().split()]
farm_times = [int(x) for x in input().split()]
required_start_times = sorted(
    [closing_times[i] - farm_times[i] - 1 for i in range(num_farms)], reverse=True
)

for _ in range(num_queries):
    num_target_farms, start_time = [int(x) for x in input().split()]

    if required_start_times[num_target_farms - 1] >= start_time:
        print("YES")
    else:
        print("NO")
