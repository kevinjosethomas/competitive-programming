import sys

input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

g = int(input())
p = int(input())
gates = [i for i in range(1, g + 1)]


def binary_search(low, high, gates, max_plane):

    if low > high:
        return False

    mid = (low + high) // 2
    mid_value = gates[mid]

    if mid_value == max_plane:
        gates.pop(mid)
        return True
    elif mid_value < max_plane:
        x = binary_search(mid + 1, high, gates, max_plane)
        if x is False:
            gates.pop(mid)
            return True
        return x
    else:
        return binary_search(low, mid - 1, gates, max_plane)


count = 0
for _ in range(p):
    max_plane = int(input())
    count += 1
    if binary_search(0, len(gates) - 1, gates, max_plane) is False:
        break

print(count - 1)
