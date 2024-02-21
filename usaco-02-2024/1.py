import math


def form_palindrome(n):
    n_str = str(n)
    palindrome_arr = [0] * len(n_str)

    for i in range(math.ceil(len(n_str) / 2)):
        palindrome_arr[i] = n_str[i]
        palindrome_arr[-i - 1] = n_str[i]

    return palindrome_arr


def find_largest_palindrome(n):
    palindrome_arr = form_palindrome(n)
    palindrome_int = int("".join(palindrome_arr))

    while palindrome_int > n:

        if palindrome_int == 11:
            palindrome_int = 9
            palindrome_arr = ["9"]
            continue

        middle = (len(palindrome_arr) - 1) // 2
        inverse_middle = -middle - 1

        while palindrome_arr[middle] == "0":
            palindrome_arr[middle] = "9"
            palindrome_arr[inverse_middle] = "9"
            middle -= 1
            inverse_middle += 1

        value = str(int(palindrome_arr[middle]) - 1)

        palindrome_arr[middle] = value
        palindrome_arr[inverse_middle] = value
        palindrome_int = int("".join(palindrome_arr))

        if middle == 0:
            palindrome_arr = form_palindrome(palindrome_int)

        palindrome_int = int("".join(palindrome_arr))

    return palindrome_int


t = int(input())
for _ in range(t):
    c = int(input())
    count = 0
    while c > 0:
        c -= find_largest_palindrome(c)
        count += 1

    if count % 2 == 0:
        print("E")
    else:
        print("B")
