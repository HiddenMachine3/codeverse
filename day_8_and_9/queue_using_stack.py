class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Stack:
    def __init__(self):
        self.curr = Node(None)

    def push(self, val):
        self.curr.next = Node(val)
        self.curr.next.prev = self.curr
        self.curr = self.curr.next

    def pop(self):
        val = self.curr.val
        if val == None:
            return val

        self.curr = self.curr.prev
        self.curr.next = None
        return val

    def top(self):
        return self.curr.val

    def __str__(self):
        string = ""
        
        temp = self.curr
        while temp.val != None:
            string = str(temp.val) + "," + string
            temp = temp.prev
        return string


class MyQueue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        self.stack1.push(x)
        # print("push called")
        # print("stack1 :", self.stack1)
        # print("stack2 :", self.stack2)


    def pop(self) -> int:
        while self.stack1.top() != None:
            self.stack2.push(self.stack1.pop())
        val = self.stack2.pop()
        while self.stack2.top() != None:
            self.stack1.push(self.stack2.pop())
        
        # print("pop called")
        # print("stack1 :", self.stack1)
        # print("stack2 :", self.stack2)
        return val

    def peek(self) -> int:
        while self.stack1.top() != None:
            self.stack2.push(self.stack1.pop())
        ele = self.stack2.top()
        while self.stack2.top() != None:
            self.stack1.push(self.stack2.pop())

        # print("peek called")
        # print("stack1 :", self.stack1)
        # print("stack2 :", self.stack2)

        return ele

    def empty(self) -> bool:
        return self.stack1.top() == None


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()