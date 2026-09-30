class Solution:
    def mySqrt(self, x: int) -> int:
        #newton raphson method
        r = x
        while r * r > x:
            r = (r + x // r) >> 1
        return r