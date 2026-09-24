class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        numeric = "0123456789"
        alphanumeric = alpha + alpha.upper() + numeric

        newS = ""
        for c in s:
            if c in alphanumeric:
                newS += c.lower()
        if newS == "":
            return True
        
        for i in range(round(len(newS)/2)+1):
            if newS[i] != newS[len(newS)-i-1]:
                return False

        return True