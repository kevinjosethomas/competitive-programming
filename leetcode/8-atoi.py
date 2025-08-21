"""
MAX_SIZE = (2**31) - 1
MIN_SIZE = -(2**31)


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        num = ""
        for index in range(len(s)):
            char = s[index]

            if index == 0:
                if char == "-":
                    num += char
                    continue
                elif char == "+":
                    continue
                elif not char.isdigit():
                    return 0

            if char.isdigit():
                num += char
            else:
                break

        try:
            parsed_num = int(num)
        except:
            parsed_num = 0

        return min(max(parsed_num, MIN_SIZE), MAX_SIZE)
"""

MAX = (2**31) - 1
MIN = -(2**31)


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = None
        num = ""

        for char in s:
            if not char.isdigit():
                if sign is None and char in ["+", "-"] and not len(num):
                    sign = 1 if char == "+" else -1
                    continue
                break

            num += char

        parsed = int(num if len(num) else 0) * (
            sign if sign is not None else 1
        )

        return min(max(parsed, MIN), MAX)
