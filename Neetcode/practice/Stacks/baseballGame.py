class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            try:
                stack.append(int(op))
            except ValueError:
                if op == "C":
                    stack.pop()
                elif op == "D":
                    stack.append(stack[-1]*2)
                else:
                    stack.append(stack[-1] + stack[-2])
        return sum(stack)