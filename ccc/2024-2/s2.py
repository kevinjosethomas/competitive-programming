t, n = [int(x) for x in input().split()]

ALPHABET = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25,
}


for _ in range(t):
    chars = [0] * 26
    inp = input()

    for char in ALPHABET.keys():
        chars[ALPHABET[char]] = inp.count(char)

    first = inp[0]
    fits = True
    heavy_first = chars[ALPHABET[first]] > 1
    for i in range(n):
        if heavy_first:  # every even index should be heavy
            if i % 2 == 0 and chars[ALPHABET[inp[i]]] <= 1:
                fits = False
                break
            elif i % 2 != 0 and chars[ALPHABET[inp[i]]] > 1:
                fits = False
                break
        else:  # every even index should be not heavy
            if i % 2 == 0 and chars[ALPHABET[inp[i]]] > 1:
                fits = False
                break
            elif i % 2 != 0 and chars[ALPHABET[inp[i]]] <= 1:
                fits = False
                break

    print("T" if fits else "F")
