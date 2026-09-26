class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        maxI = 0
        for word in strs:
            maxI = max(maxI, len(word))
        
        while i <= maxI:
            for word in strs:
                if strs[0][:i] != word[:i]:
                    i -= 1
                    return strs[0][:i]
            i += 1
        
        return strs[0][:i]