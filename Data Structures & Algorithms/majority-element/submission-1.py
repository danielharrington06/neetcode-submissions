class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        currNum = None
        count = 0
        for num in nums:
            if count == 0:
                currNum = num
            count += (1 if num == currNum else -1)
        
        return currNum