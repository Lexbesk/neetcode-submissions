class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [(0, 0, -1)] # (height, left_width, i)
        max_rect = 0
        for i in range(len(heights)):
            left_width = 0
            while heights[i] < stack[-1][0]:
                new_max_rect = stack[-1][0] * (i - stack[-1][2] + stack[-1][1])
                print(new_max_rect)
                max_rect = max(max_rect, new_max_rect)
                left_width += stack[-1][1] + 1
                stack = stack[:-1]
            stack.append((heights[i], left_width, i))
        return max_rect
