i = input()
h, v = i.count("H") % 2, i.count("V") % 2
grid = [["1", "2"], ["3", "4"]]

if h:
    grid = [grid[1], grid[0]]
if v:
    grid = [[grid[0][1], grid[0][0]], [grid[1][1], grid[1][0]]]

for line in grid:
    print(" ".join(line))
