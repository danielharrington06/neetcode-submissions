class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        currNum = None
        count = 0
        for num in nums:
            if count == 0:
                currNum = num
                count += 1
            elif num != currNum:
                count -= 1
            else:
                count += 1
        
        return currNum