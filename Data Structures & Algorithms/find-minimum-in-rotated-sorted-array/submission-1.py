class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            print(l, r)
            if l == r:
                return nums[l]
            elif nums[l] <= nums[mid]:
                if nums[l] <= nums[r]:
                    return nums[l]
                else:
                    l = mid + 1
            elif nums[mid] <= nums[r]:
                if nums[l] <= nums[r]:
                    r = mid - 1
                else:
                    r = mid

        return -1