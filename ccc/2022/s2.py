x = int(input())
same_group = [input().split() for _ in range(x)]
same = {}
for relation in same_group:
    if same.get(relation[0]):
        same[relation[0]].append(relation[1])
    else:
        same[relation[0]] = [relation[1]]
    if same.get(relation[1]):
        same[relation[1]].append(relation[0])
    else:
        same[relation[1]] = [relation[0]]

y = int(input())
different_group = [input().split() for _ in range(y)]
different = {}
for relation in different_group:
    if different.get(relation[0]):
        different[relation[0]].append(relation[1])
    else:
        different[relation[0]] = [relation[1]]
    if different.get(relation[1]):
        different[relation[1]].append(relation[0])
    else:
        different[relation[1]] = [relation[0]]

g = int(input())
groups = [input().split() for _ in range(g)]

violations = 0
for group in groups:
    for member in group:

        same_restrictions = same.get(member, [])
        for same_member in same_restrictions:
            if same_member not in group:
                violations += 1

        different_restrictions = different.get(member, [])
        for different_member in different_restrictions:
            if different_member in group:
                violations += 1

print(violations // 2)
