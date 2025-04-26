from collections import deque
class MyStack:

    def __init__(self):
        self.stack = deque()
        
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        try:
            ele = self.stack.pop()
            self.stack.append(ele)
            return ele
        except IndexError:
            return None

    def empty(self) -> bool:
        if self.top() != None:
            return False
        return True