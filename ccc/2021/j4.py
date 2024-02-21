bookshelf = input()

sorted_bookshelf = (
    bookshelf.count("L") * "L" + bookshelf.count("M") * "M" + bookshelf.count("S") * "S"
)

mismatched_count = 0
for index, x in enumerate(sorted_bookshelf):
    if x != bookshelf[index]:
        mismatched_count += 1

print(mismatched_count // 2)
