class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        nonZeroProd = 1
        seenZero = False
        for num in nums:
            prod *= num
            if num != 0 or seenZero:
                nonZeroProd *= num
            if num == 0:
                seenZero = True

        if seenZero:
            result = [nonZeroProd if n == 0 else 0 for n in nums]
        else:
            result = [int(prod/n) for n in nums]
        return result