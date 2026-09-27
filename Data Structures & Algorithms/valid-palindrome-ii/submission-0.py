class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = [0,0]
        r = [len(s) - 1, len(s)-1]
        skipped = False
        while l[0] < r[0] and l[1] < r[1]:
            print(l, r)
            if not skipped:
                if s[l[0]] != s[r[0]]:
                    skipped = True
                    l[0] += 1
                    r[1] -= 1
                else:
                    l[0] += 1
                    l[1] += 1
                    r[0] -= 1
                    r[1] -= 1
            else:
                if s[l[0]] != s[r[0]] and s[l[1]] != s[r[1]]:
                    return False
                if s[l[0]] == s[r[0]]:
                    # dont increment so it gets stuck
                    l[0] += 1
                    r[0] -= 1
                if s[l[1]] == s[r[1]]:
                    l[1] += 1
                    r[1] -= 1
        return True

