import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = math.floor(sum(piles)/h)
        upper = max(piles)
        while lower <= upper:
            mid = (lower + upper) // 2
            if lower == upper:
                return lower
            elif self.works(piles, h, mid):
                upper = mid
            else:
                lower = mid + 1
        return 0
    def works(self, piles, h, k):
        if k == 0:
            return False
        count = 0
        for pile in piles:
            count += math.ceil(pile/k)


        return count <= h
            