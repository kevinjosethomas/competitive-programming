spotcount, marblecount = [int(x) for x in input().split()]
marbles = list(input())


def merge(marbles):
    for i in range(len(marbles) - 1):
        if marbles[i + 1] == "1":
            marbles[i] = "0"


def find_bounds(index, marbles):
    zeroes = 1
    trailing_ones = 0
    leading_ones = 0
    peaked = False

    var_index = index
    while True:
        var_index -= 1

        if var_index < 0:
            break

        if peaked:
            if marbles[var_index] == "0":
                break
            else:
                trailing_ones += 1
        else:
            if marbles[var_index] == "0":
                zeroes += 1
            else:
                peaked = True
                trailing_ones += 1

    var_index = index
    peaked = False
    while True:
        var_index += 1

        if var_index >= len(marbles):
            break

        if peaked:
            if marbles[var_index] == "0":
                break
            else:
                leading_ones += 1
        else:
            if marbles[var_index] == "0":
                zeroes += 1
            else:
                peaked = True
                leading_ones += 1

    impact = trailing_ones + leading_ones

    return (zeroes, impact, index)


while marblecount > 0:
    merge(marbles)

    queue = []

    starting_points = [
        i
        for i, x in enumerate(marbles)
        if x == "0" and (i == 0 or marbles[i - 1] == "1")
    ]

    for point in starting_points:
        queue.append(find_bounds(point, marbles))

    queue.sort(key=lambda x: (x[0], -x[1]))

    optimal = None

    for x in queue:
        if x[0] <= marblecount:
            optimal = x
            break

    if not optimal:
        optimal = queue[0]

    for i in range(optimal[2] + optimal[0] - 1, optimal[2] - 1, -1):
        if marblecount <= 0:
            break

        marbles[i] = "1"
        marblecount -= 1

merge(marbles)
print(marbles.count("1"))
