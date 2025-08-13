class Solution:
    def longestPalindrome(self, s: str) -> str:
        for length in range(len(s), 1, -1):
            for start in range(0, len(s) - length + 1):
                left = s[start : start + (length // 2)]
                right = (
                    s[
                        start
                        + (length // 2)
                        + (1 if length % 2 != 0 else 0) : start
                        + length
                    ]
                )[::-1]

                if left == right:
                    return s[start : start + length]

        return s[0]
