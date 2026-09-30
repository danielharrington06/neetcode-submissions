class Solution:
    def mySqrt(self, x: int) -> int:
        #naive approach
        r = x
        while r * r > x:
            r = (r + x // r) >> 1
        return r