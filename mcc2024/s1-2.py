import heapq

sp, mb = [int(x) for x in input().split()]
marbles = list(input())


def merge(mbles):
    for i in range(len(mbles) - 1):
        if mbles[i + 1] == "1":
            mbles[i] = "0"

    return mbles


while mb > 0:
    marbles = merge(marbles)

    queue = []
    heapq.heapify(queue)

    count = None
    for i, c in enumerate(marbles):
        if c == "0":
            if count:
                count[0] = count[0] + 1
            else:
                count = [1, i]
        else:
            if count:
                heapq.heappush(queue, count)
                count = None

    optimal = heapq.heappop(queue)

    while optimal[0] > mb:
        optimal = heapq.heappop(queue)

    marbles[optimal[1] : optimal[1] + optimal[0]] = "1"
    mb -= optimal[0]

marbles = merge(marbles)
print(marbles.count("1"))
