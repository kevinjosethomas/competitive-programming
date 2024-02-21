num = int(input())
times = [[int(x) for x in input().split()] for _ in range(num)]

times.sort(key=lambda x: x[0])

speeds = []

for i in range(1, num):
    prev = times[i - 1]
    current = times[i]
    speeds.append(abs((current[1] - prev[1]) / (current[0] - prev[0])))

print(max(speeds))
