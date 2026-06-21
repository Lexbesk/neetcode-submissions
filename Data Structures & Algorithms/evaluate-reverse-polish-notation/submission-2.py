class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                res = stack[-2] + stack[-1]
                stack = stack[:-2]
                stack.append(res)
            elif tokens[i] == '-':
                res = stack[-2] - stack[-1]
                stack = stack[:-2]
                stack.append(res)
            elif tokens[i] == '*':
                res = stack[-2] * stack[-1]
                stack = stack[:-2]
                stack.append(res)
            elif tokens[i] == '/':
                res = int(stack[-2] / stack[-1])
                stack = stack[:-2]
                stack.append(res)
            else:
                stack.append(int(tokens[i]))
        return stack[0]
                