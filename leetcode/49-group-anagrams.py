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
