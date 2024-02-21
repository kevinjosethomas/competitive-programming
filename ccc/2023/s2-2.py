n = int(input())
mountains = [int(x) for x in input().split()]


def calculate_symmetry(m):
    total = 0
    for i in range(len(m) // 2):

        total += abs(m[i] - m[-i - 1])

    return total


crops = []

for cropsize in range(1, n + 1):
    smallest = None
    crop = mountains[0:cropsize]

    for i in range(0, n - cropsize + 1):
        x = calculate_symmetry(crop)

        if smallest is None or x < smallest:
            smallest = x

        if i + cropsize > n - 1:
            break

        crop.pop(0)
        crop.append(mountains[i + cropsize])

    crops.append(str(smallest))

print(" ".join(crops))
