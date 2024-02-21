import math

n = int(input())
explosions = [int(input()) for _ in range(n)]
explosions.sort()
explosions.pop(-1)
print(math.floor(sum(explosions) / len(explosions)))
