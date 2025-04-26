class MyCircularQueue:

    def __init__(self, k: int):
        
        self.queue = [None]*k
        self.front = 0
        self.rear = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        next_idx = (self.front + 1) % self.k if not self.isEmpty() else self.front
        if self.queue[next_idx] == None:
            self.queue[next_idx] = value
            self.front = next_idx
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.queue[self.rear] != None:
            val = self.queue[self.rear]
            self.queue[self.rear] = None
            if self.rear!=self.front:
                self.rear += 1
                self.rear %= self.k
            return True
        else:
            return False

    def Front(self) -> int:
        ele = self.queue[self.rear]
        return ele if ele!=None else -1

    def Rear(self) -> int:
        # print("rear called", self.queue)
        ele = self.queue[self.front]
        return ele if ele!=None else -1

    def isEmpty(self) -> bool:
        return self.queue[self.rear] == None

    def isFull(self) -> bool:
        next_idx = (self.front + 1) % self.k
        return self.queue[next_idx] != None


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()