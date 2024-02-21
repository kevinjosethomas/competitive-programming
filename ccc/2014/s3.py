import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    mountaintop = deque([int(input()) for _ in range(n)])
    branch = deque([])
    lake = deque([])

    while len(lake) < n:

        if lake:
            target = lake[0] + 1
        else:
            target = 1

        if mountaintop:
            if target == mountaintop[-1]:  # move from mountaintop to lake
                car = mountaintop.pop()
                lake.appendleft(car)
                continue

        if branch:
            if target == branch[0]:  # move from branch to lake
                car = branch.popleft()
                lake.appendleft(car)
                continue

        if mountaintop:
            car = mountaintop.pop()
            branch.appendleft(car)
        else:
            print("N")
            break

    if len(lake) == n:
        print("Y")
