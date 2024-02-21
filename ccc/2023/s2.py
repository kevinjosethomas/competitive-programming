n = int(input())
mountains = [int(x) for x in input().split()]

symmetry = [[None for _ in range(n)] for __ in range(n)]


def find_symmetry(start, end, size):
    total = 0
    for k in range(size // 2):
        i = start + k
        j = end - k

        if symmetry[i][j] is not None:
            total += symmetry[i][j]
            break

        total += abs(mountains[start + k] - mountains[end - k])

    symmetry[start][end] = total

    return total


for window_size in range(1, n + 1):
    smallest = None
    for i in range(n - window_size + 1):
        j = i + window_size - 1
        symm = find_symmetry(i, j, window_size)

        if smallest is None or symm < smallest:
            smallest = symm

    print(smallest, end=" ")
