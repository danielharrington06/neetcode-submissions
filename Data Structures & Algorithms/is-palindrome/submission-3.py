class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        numeric = "0123456789"
        alphanumeric = alpha + alpha.upper() + numeric

        forward = ""
        for c in s:
            if c in alphanumeric:
                forward += c.lower()
        
        reverse = forward[::-1]

        return reverse == forward