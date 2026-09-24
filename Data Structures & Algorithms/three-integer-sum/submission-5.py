class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]

            while j < k:
                total = nums[j] + nums[k]

                if total == target:
                    arr = [nums[i], nums[j], nums[k]]
                    arr.sort()
                    if arr == [-4,2,2]:
                        print(i,j,k)

                    if arr not in result:
                        result.append(arr)
                    j += 1
                    k -= 1
                elif total > target:
                    k -= 1
                else:
                    j += 1

        return result       
                    