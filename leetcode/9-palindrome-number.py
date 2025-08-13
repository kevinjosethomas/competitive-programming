class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        left = s[: len(s) // 2]
        right = s[len(s) // 2 + (1 if len(s) % 2 == 0 else 0) :][::-1]

        return left == right
