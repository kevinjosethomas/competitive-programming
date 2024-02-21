import sys
from time import perf_counter


def input():
    return sys.stdin.readline().strip()


n, k = [int(x) for x in input().split()]
testcase = [int(x) for x in input().split()]
sum_testcase = sum(testcase)
x_values = [int(x) for x in input().split()]

full = perf_counter()
for d in range(1, k + 1):
    t = perf_counter()

    x_d = x_values[d - 1]
    purged_testcase = []
    purged_sum = sum_testcase

    for a in testcase:
        if a != d:
            purged_testcase.append(a)
        else:
            purged_sum -= d
            for _ in range(x_d):
                if purged_testcase:
                    purged_sum -= purged_testcase.pop(-1)

    print(perf_counter() - t)

print(perf_counter() - full)
