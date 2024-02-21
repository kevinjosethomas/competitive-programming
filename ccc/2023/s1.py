cols = int(input())
row1 = [int(x) for x in input().split()]
row2 = [int(x) for x in input().split()]

border = 0

for i, col in enumerate(row1):
    """
    Even faces up
    Odd faces down
    """

    if col == 0:  # if not painted
        if i != 0 and row1[i - 1] == 1:
            border += 1
        continue

    if i == 0 or row1[i - 1] == 0:  # if first or if previous not painted
        border += 1

    if i % 2 == 0:  # if faces up
        if row2[i] == 0:  #  if under is not painted
            border += 1
    else:  # if faces down
        border += 1

    if i == cols - 1:  # if last
        border += 1

for i, col in enumerate(row2):
    """
    Even faces down
    Odd faces up
    """

    if col == 0:  # if not painted
        if i != 0 and row2[i - 1] == 1:
            border += 1
        continue

    if i == 0 or row2[i - 1] == 0:  # if first or if previous not painted
        border += 1

    if i % 2 != 0:  # if faces up
        border += 1
    else:  # if faces down
        if row1[i] == 0:
            border += 1

    if i == cols - 1:
        border += 1

print(border)
