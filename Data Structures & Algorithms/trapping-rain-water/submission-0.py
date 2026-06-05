class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        left_highest_bar = [0 for i in range(l)]
        right_highest_bar = [0 for i in range(l)]
        
        left_highest = 0
        for i in range(l):
            left_highest_bar[i] = left_highest
            left_highest = max(left_highest, height[i])

        right_highest = 0
        for i in range(l):
            right_highest_bar[l - 1 - i] = right_highest
            right_highest = max(right_highest, height[l - 1 - i])
        
        rain_area = 0
        for i in range(l):
            rain_area += max(0, min(left_highest_bar[i], right_highest_bar[i]) - height[i])
        
        return rain_area