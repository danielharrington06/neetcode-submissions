class Solution:
    # structure: .length:string.length:string.length:string

    def encode(self, strs: List[str]) -> str:
        encoded = "S"
        for string in strs:
            encoded = encoded + "." + str(len(string)) 
            encoded = encoded + ":" + string
        encoded = encoded + "!E"
        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        if s[0] != "S":
            return None

        s = s[1:]
        i = 0

        while s[i] == ".":
            i += 1
            
            num = ""
            while s[i] != ":":
                num += s[i]
                i += 1
            num = int(num)

            if s[i] != ":":
                return None
            i += 1

            string = ""
            for j in range(num):
                string += s[i]
                i += 1
            strs.append(string)
        return strs
