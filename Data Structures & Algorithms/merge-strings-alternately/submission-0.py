class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        result = ""
        n = min(len(word1), len(word2))
        while i < n:
            result += word1[i] + word2[i]
            i += 1
        
        result += word1[i:] + word2[i:]

        return result