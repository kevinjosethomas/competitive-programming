n = int(input())
poll = list(input())
min_majority = (n // 2) + 1

try:
    last_y_1_indexed = n - list(reversed(poll)).index("Y")

    if last_y_1_indexed >= min_majority:
        print("YES")
    else:
        print("NO")
except ValueError:
    print("NO")
