class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left_brackets = ['(', '[', '{']
        right_brackets = [')', ']', '}']
        for char in s:
            if char in left_brackets:
                stack.append(char)
            elif char in right_brackets:
                if char == ')':
                    if not stack or stack[-1] != '(':
                        return False
                    stack = stack[:-1]
                elif char == ']':
                    if not stack or stack[-1] != '[':
                        return False
                    stack = stack[:-1]
                elif char == '}':
                    if not stack or stack[-1] != '{':
                        return False
                    stack = stack[:-1]
        if not stack:
            return True
        else:
            return False