n = int(input())
heights = [int(x) for x in input().split()]
widths = [int(x) for x in input().split()]

area = 0

for i in range(n):
    width = widths[i]
    left = heights[i]
    right = heights[i + 1]

    area += (width * min(left, right)) + (
        max(left, right) - min(left, right)
    ) * width * 0.5

print(area)
