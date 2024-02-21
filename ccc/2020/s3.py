ALPHABET = "abcdefghijklmnopqrstuvwxyz"

needle = input()
haystack = input()

needle_size = len(needle)
haystack_size = len(haystack)
discovered_needles = set([])

p = 31
m = 10**9 + 9


def hash_string(string):
    p_pow = 1
    hash_value = 0

    for char in string:
        hash_value = (hash_value + ord(char) * p_pow) % m
        p_pow = (p_pow * p) % m

    return hash_value


needle_count = [0] * 26
for letter in needle:
    needle_count[ord(letter) - 97] += 1

first_needle = {}

letter_count = [0] * 26

for i in range(haystack_size - (needle_size - 1)):
    possible_needle = haystack[i : i + needle_size]

    if i == 0:
        for letter in possible_needle:
            letter_count[ord(letter) - 97] += 1
    else:
        letter_count[ord(haystack[i - 1]) - 97] -= 1
        letter_count[ord(haystack[i + needle_size - 1]) - 97] += 1

    if letter_count != needle_count:
        continue

    hash_value = hash(possible_needle)

    discovered_needles.add(hash_value)

print(len(discovered_needles))
