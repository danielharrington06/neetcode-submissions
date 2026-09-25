class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        r = 0
        sub = s[0:0]
        while r < len(s):
            if s[r] not in sub or l == r:
                r += 1
            else:
                l += 1
            sub = s[l:r]
            longest = max(longest, len(sub))
        return longest