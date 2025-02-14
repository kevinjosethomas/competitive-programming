numbers = [int(input()) for _ in range(int(input()))]
opposite_distance = len(numbers) // 2

count = 0

for i in range(opposite_distance):
    count += 1 if numbers[i] == numbers[i + opposite_distance] else 0

print(count * 2)
