# O(n^3)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        for length in range(len(s), 0, -1):
            for start in range(0, len(s) - length + 1):
                l = list(s[start : start + length])
                setted = set(l)
                if len(l) == len(setted):
                    return length

        return 0
"""

# O(n^2
"""
def create_frequency_table(s: str):
    table = {}

    for char in s:
        if table.get(char):
            table[char] += 1
        else:
            table[char] = 1

    return table


def check_repeating(table: dict):
    values = list(filter(lambda x: x > 1, table.values()))
    return bool(len(values))


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        for length in range(len(s), 0, -1):
            table = create_frequency_table(s[:length])

            if not check_repeating(table):
                return length

            for start in range(1, len(s) - length + 1):
                table[s[start - 1]] -= 1
                new_char = s[start + length - 1]
                if table.get(new_char):
                    table[new_char] += 1
                else:
                    table[new_char] = 1

                if not check_repeating(table):
                    return length

        return 0
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        vals = set()
        longest = 0
        left = 0

        for right in range(len(s)):
            while s[right] in vals:
                vals.remove(s[left])
                left += 1

            vals.add(s[right])
            longest = max(longest, right - left + 1)

        return longest
