class Solution:
    def countAndSay(self, n: int) -> str:

        def rle(s: str):
            parsed = ""

            char = None
            count = 0

            for i, c in enumerate(s):

                if char is None:
                    char = c
                    count += 1
                    continue

                if c == char:
                    count += 1
                else:
                    parsed += f"{str(count)}{char}"
                    char = c
                    count = 1

            parsed += f"{str(count)}{char}"

            return parsed

        cache = {1: "1"}
        for i in range(2, n + 1):
            cache[i] = rle(cache[i - 1])

        return cache[n]
