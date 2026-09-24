class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        least = min(nums)
        most = max(nums)

        buckets = []
        for i in range(least, most+1):
            buckets.append(0)
        
        for n in nums:
            buckets[n - least] += 1
        
        maxN = max(buckets)
        result = []
        for i in range(maxN, 0, -1):
            for j, val in enumerate(buckets):
                if val == i:
                    result.append(j+least)
            if len(result) >= k:
                return result
        
        return result