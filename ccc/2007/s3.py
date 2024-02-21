num_of_students = int(input())
students = {}
for _ in range(num_of_students):
    i = input().split()
    students[i[0]] = i[1]

while True:
    one, two = input().split()

    if one == "0" and two == "0":
        break

    connected = False
    connected_index = None
    visited = []
    queue = [students[one]]
    while True:
        nxt = queue.pop(0)
        visited.append(nxt)
        queue.append(students[nxt])

        if nxt == two:
            connected = True
            connected_index = len(visited)

        if nxt in visited:
            if not connected:
                print("No")
                break

            if connected_index < visited.index(nxt):
                print("No")
                break

            print(f"Yes {connected_index-1}")
            break
