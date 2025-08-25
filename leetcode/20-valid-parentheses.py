class Solution:
    def isValid(self, s: str) -> bool:
        o = ["(", "{", "]"]
        c = [")", "}", "]"]
        n = []

        for char in s:
            if char in o:
                if char == "(":
                    n.append(")")
                elif char == "{":
                    n.append("}")
                else:
                    n.append("]")
            else:

                if char != n.pop(-1):
                    return False

        return True
