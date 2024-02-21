import sys

input = sys.stdin.readline

n, s, t = [int(x) for x in input().strip().split()]
powers = [int(x) for x in input().strip().split()]
powers_sum = []
for i, x in enumerate(powers):
    if i == 0:
        powers_sum.append(x)
        continue
    powers_sum.append(x + powers_sum[i - 1])

damage = []
for i in range(t + 1):
    left = s * (t - i)
    right = (t * s) - left

    if left <= 0:
        leftsum = 0
    elif left >= len(powers_sum):
        leftsum = powers_sum[-1]
        damage = [leftsum]
        break
    else:
        leftsum = powers_sum[left - 1]

    if right >= len(powers_sum):
        rightsum = powers_sum[-1]
    else:
        rightsum = powers_sum[-1] - powers_sum[-right - 1]

    damage.append(leftsum + rightsum)

print(max(damage))
