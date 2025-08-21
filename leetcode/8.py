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
