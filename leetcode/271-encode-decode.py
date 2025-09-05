from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        return ",".join([str(len(x)) for x in strs]) + "|" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        metadata = []

        data = ""
        breakstart = None
        for i, char in enumerate(s):
            if char == "|":
                if data:
                    metadata.append(int(data))
                    breakstart = i + 1
                break

            if char == ",":
                if data:
                    metadata.append(int(data))
                    data = ""
                continue

            data += char

        l = []
        for length in metadata:
            l.append(s[breakstart : breakstart + length])
            breakstart += length

        return l
