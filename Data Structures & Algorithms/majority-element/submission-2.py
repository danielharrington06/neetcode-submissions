class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = nums[0]
        count = 0
        for num in nums:
            if count == 0:
                curr = num
                count += 1
            elif num == curr:
                count += 1
            else:
                count -= 1
        
        return curr