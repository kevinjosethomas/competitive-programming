directions = []

while True:
    direction = input()
    if direction == "99999":
        break
    directions.append(direction)

previous_turn = None
for direction in directions:
    turn = int(direction[0]) + int(direction[1])
    if turn == 0:  # sum is 0
        turn = previous_turn
    elif turn % 2 == 0:  # sum is even
        turn = "right"
    else:  # sum is odd
        turn = "left"
    previous_turn = turn

    print(f"{turn} {direction[2:]}")
