spotcount, marblecount = [int(x) for x in input().split()]
marbles = list(input())


def merge(marbles):
    for i in range(len(marbles) - 1):
        if marbles[i + 1] == "1":
            marbles[i] = "0"


merge(marbles)

for _ in range(marblecount):

    real_marbles = [i for i, x in enumerate(marbles) if x == "1"]
    prefix_diff_array = sorted(
        [
            (real_marbles[i] - real_marbles[i - 1] - 1, real_marbles[i - 1] + 1)
            for i in range(1, len(real_marbles))
        ],
        key=lambda x: x[0],
    )

    index = None
    if prefix_diff_array:
        index = prefix_diff_array[0][1]

    else:
        if real_marbles:
            if real_marbles[0] <= 0:
                index = real_marbles[0] + 1
            else:
                index = real_marbles[0] - 1
        else:
            index = -1

    marbles[index] = "1"
    merge(marbles)

print(marbles.count("1"))
