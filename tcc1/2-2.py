import sys


def input():
    return sys.stdin.readline().strip()


n, k = [int(x) for x in input().split()]
testcase = [int(x) for x in input().split()]
x_values = [int(x) for x in input().split()]

for d in range(1, k + 1):
    x_d = x_values[d - 1]
    purged_sum = 0
    ignore_queue = 0

    for a in range(n - 1, -1, -1):

        if testcase[a] == d:
            ignore_queue += x_d
        else:
            if ignore_queue:
                ignore_queue -= 1
                continue
            else:
                purged_sum += testcase[a]

    print(purged_sum)
