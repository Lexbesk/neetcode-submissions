class MinStack:

    def __init__(self):
        self.stack = []
        self.min_values = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_values and val > self.min_values[-1]:
            self.min_values.append(self.min_values[-1])
        else:
            self.min_values.append(val)

    def pop(self) -> None:
        res = self.stack[-1]
        self.stack = self.stack[:-1]
        self.min_values = self.min_values[:-1]
        return res

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1]
        
