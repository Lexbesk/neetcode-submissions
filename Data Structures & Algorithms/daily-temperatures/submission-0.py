class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for i in range(len(temperatures))]
        stack = [(float('inf'), -1)]
        for i in range(len(temperatures)):
            a = temperatures[i]
            while a > stack[-1][0]:
                result[stack[-1][1]] = i - stack[-1][1]
                stack = stack[:-1]
            stack.append((a, i))
        return result
            
