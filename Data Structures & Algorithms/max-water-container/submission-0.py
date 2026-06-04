class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        left_cur_height = heights[0]
        right_cur_height = heights[-1]
        max_amount = 0

        while i < j:
            cur_amount = min(heights[i], heights[j]) * (j - i)
            max_amount = max(cur_amount, max_amount)
            if heights[i] <= heights[j]:
                # move the left bar to the next one
                while i < j and heights[i] <= left_cur_height:
                    i += 1
            else:
                while i < j and heights[j] <= right_cur_height:
                    j -= 1
            left_cur_height = heights[i]
            right_cur_height = heights[j]

        return max_amount

                

