class Solution:
    def mySqrt(self, x: int) -> int:
        #naive approach
        sqr = 0
        incr = 1
        count = 0
        while sqr <= x:
            sqr += incr
            incr += 2
            count += 1
        return count - 1