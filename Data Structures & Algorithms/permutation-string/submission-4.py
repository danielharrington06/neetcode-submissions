class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Chars = dict()
        for c in s1:
            s1Chars[c] = 1 + s1Chars.get(c, 0)
        for i in range(len(s2)-len(s1)+1):
            sub = s2[i:i+len(s1)]
            print(sub)
            subChars = dict()
            for c in sub:
                subChars[c] = 1 + subChars.get(c, 0)
            if s1Chars == subChars:
                return True
        
        return False