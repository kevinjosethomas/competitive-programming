test_count, char_count = [int(x) for x in input().split()]

for _ in range(test_count):
    frequency = [0] * 26
    string = input()

    for char in string:
        frequency[ord(char) - 97] += 1

    alternate = True
    previous = -1
    for i, char in enumerate(string):
        current = -1
        if frequency[ord(char) - 97] > 1:
            current = 1  # heavy
        else:
            current = 0  # light

        if previous == -1:
            previous = current
        elif previous == current:
            alternate = False
            break
        else:
            previous = current

    if alternate:
        print("T")
    else:
        print("F")
