class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = dict()
        for l in s:
            if l not in letters:
                letters[l] = 1
            else:
                letters[l] += 1
        
        for l in t:
            if l not in letters:
                return False
            else:
                letters[l] -= 1
        
        for l in letters:
            print(f"{l}, {letters[l]}")

        for l in letters:
            print(f"{l}, {letters[l]}")
            if letters[l] != 0:
                return False
        return True
