import math

n = int(input())
tides = sorted([int(x) for x in input().split()])
low = tides[:math.ceil(len(tides)/2)][::-1]
high = tides[math.ceil(len(tides)/2):]

sorted_tides = []
for i in range(len(low)):
    sorted_tides.append(low[i])
    try:
        sorted_tides.append(high[i])
    except IndexError:
        pass

print(" ".join([str(x) for x in sorted_tides]))

