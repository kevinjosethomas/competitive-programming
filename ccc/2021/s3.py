n = int(input())
people = []

mint = None
maxt = None

for _ in range(n):
    person = [int(x) for x in input().split()]

    if mint is None or person[0] < mint:
        mint = person[0]

    if maxt is None or person[0] > maxt:
        maxt = person[0]

    people.append(person)


def find_time(c):
    total_seconds = 0

    for person in people:
        raw_distance = abs(c - person[0])

        if raw_distance <= person[2]:
            continue

        distance = raw_distance - person[2]
        time = distance * person[1]

        total_seconds += time

    return total_seconds


def orient(start, stop):
    midpoint = (stop + start) // 2
    midpoint2 = midpoint + 1

    midpoint_time = find_time(midpoint)
    midpoint2_time = find_time(midpoint2)

    if midpoint_time < midpoint2_time:
        if start == midpoint:
            return midpoint_time

        return orient(start, midpoint)
    elif midpoint_time > midpoint2_time:
        if stop == midpoint2:
            return midpoint2_time

        return orient(midpoint2, stop)
    else:
        return midpoint_time


print(orient(mint, maxt))
