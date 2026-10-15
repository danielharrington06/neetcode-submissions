class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums) - 1
        i = 0
        while i <= j:
            print(nums, i, j)
            if nums[j] == val:
                j -= 1
            elif nums[i] == val:
                # swap with last
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                i += 1
            else:
                i += 1
        res = j + 1
        return res