class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 1
        longest = max([len(s) for s in strs])
        while i <= longest:
            for s in strs:
                if s[:i] != strs[0][:i]:
                    return strs[0][:i-1]
            i += 1
        return strs[0][:i-1]