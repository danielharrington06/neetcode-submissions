class Solution:
    def mySqrt(self, x: int) -> int:
        #naive approach
        i = 0
        while i*i <= x:
            i += 1
        return i-1