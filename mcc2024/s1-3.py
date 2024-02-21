import heapq

spotcount, marblecount = [int(x) for x in input().split()]
marbles = list(input())


def merge(marbles):
    for i in range(len(marbles) - 1):
        if marbles[i] == "1" and marbles[i + 1] == "1":
            marbles[i] = "0"


while marblecount > 0:
    merge(marbles)

    queue = []
    heapq.heapify(queue)

    i = 0
    while True:

        if i >= len(marbles):
            break

        trailing_1s = 0
        zeros = 0
        leading_1s = 0

        if marbles[i] == "1":
            i += 1
            continue
        else:
            zeros += 1

        j = i
        while True:
            j -= 1

            if j < 0:
                break

            if marbles[j] == "0":
                break

            trailing_1s += 1

        j = i
        peaked = False
        while True:
            j += 1

            if j >= len(marbles):
                break

            if marbles[j] == "0":
                if peaked:
                    break
                else:
                    zeros += 1
            else:
                peaked = True
                leading_1s += 1

        i += zeros

        heapq.heappush(queue, (-trailing_1s - leading_1s, zeros, i))

    optimal = heapq.heappop(queue)

    while optimal[1] > marblecount:
        optimal = heapq.heappop(queue)

    print("".join(marbles))

    print(optimal)

    for j in range(optimal[2], optimal[2] + optimal[1]):
        marbles[j] = "1"
        marblecount -= 1
    print("".join(marbles))
    print("\n")

merge(marbles)
print(marbles.count("1"))
