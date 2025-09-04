# O(n*m*log(m))
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lib = {}

        for s in strs:
            parsed = "".join(sorted(s))
            if lib.get(parsed):
                lib[parsed].append(s)
            else:
                lib[parsed] = [s]

        return [x for x in lib.values()]
"""

# O(n*m)
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lib = {}

        for s in strs:
            alphabet = [0] * 26
            for char in s:
                alphabet[ord(char) - 97] += 1
            tupled = tuple(alphabet)
            if lib.get(tupled):
                lib[tupled].append(s)
            else:
                lib[tupled] = [s]

        return [x for x in lib.values()]
