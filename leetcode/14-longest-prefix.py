from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for length in range(len(min(strs, key=len))):
            for string in strs:
                if string[length] != strs[0][length]:
                    return strs[0][:length]

        return min(strs, key=len)
