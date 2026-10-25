class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + ","
            res += s + ","
        res += "f"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            if s[i] == "f":
                break

            length = ""
            while s[i] != ",":
                length += s[i]
                i += 1
            length = int(length)
            i += 1

            word = s[i:i+length]
            i += length + 1

            res.append(word)
        return res