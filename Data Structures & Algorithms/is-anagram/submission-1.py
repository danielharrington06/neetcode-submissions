class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = dict()
        for c in s:
            letters[c] = 1 + letters.get(c, 0)
        for c in t:
            if letters.get(c, 0) == 0:
                return False
            else:
                letters[c] = letters[c] - 1
        
        for c in letters:
            if letters[c] != 0:
                return False
        
        return True
