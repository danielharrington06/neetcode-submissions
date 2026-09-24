class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = dict()

        for i in range(len(nums)):
            difference = target - nums[i]
            if target - difference in hashmap:
                return [hashmap[target - difference], i]
            else:
                hashmap[difference] = i
        for dif in hashmap:
            print(dif, hashmap[dif])