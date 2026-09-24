class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums.sort()
        longest = 1
        curr = 1
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                curr += 1
            elif nums[i] == nums[i-1]:
                curr += 0
            else:
                if curr > longest:
                    longest = curr
                curr = 1
        if curr > longest:
            longest = curr
        return longest
                