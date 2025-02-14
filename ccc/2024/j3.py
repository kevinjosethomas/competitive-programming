scores = sorted([int(input()) for _ in range(int(input()))], reverse=True)
print(
    sorted(list(set(scores)), reverse=True)[2],
    scores.count(sorted(list(set(scores)), reverse=True)[2]),
)
