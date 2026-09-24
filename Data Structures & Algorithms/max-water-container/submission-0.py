class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1

        mostWater = 0
        while i < j:
            water = min(heights[i],heights[j]) * (j-i)
            mostWater = max(mostWater, water)
            if heights[i] <= heights[j]:
                i += 1
            elif heights[j] < heights[i]:
                j -= 1
        
        return mostWater