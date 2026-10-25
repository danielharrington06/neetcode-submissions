class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = {
            0: 0,
            1: 0,
            2: 0
        }
        for num in nums:
            count[num] += 1
        print(count)
        i = 0
        for c in count:
            print(i, c, count[c])
            for j in range(i, i+count[c]):
                nums[j] = c
            i += count[c]

        