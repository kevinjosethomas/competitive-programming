import math

n = int(input())
nums = [int(input()) * 2 for _ in range(n)]


def is_prime(x):
    if x == 2:
        return True

    for f in range(2, math.ceil(math.sqrt(x)) + 1):
        if x % f == 0:
            return False

    return True


solutions = []

for num in nums:
    for i in range(2, (num // 2) + 1):
        prime = is_prime(i)

        if not prime:
            continue

        addend = num - i
        if is_prime(addend):
            solutions.append((str(i), str(addend)))
            break

for solution in solutions:
    print(" ".join(solution))
