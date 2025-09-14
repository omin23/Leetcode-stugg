class Node():
    def __init__(self, val):
        self.next, self.val = None, val
    
class MyCircularQueue:
    def __init__(self, k: int):
        self.total_nodes = k
        self.num_nodes_avail = k

        # creates the linked list 
        self.front = Node(float("inf"))
        curr = self.front
        for i in range(k-1):
            curr.next = Node(float("inf"))
            curr = curr.next
        curr.next = self.front
        self.back = self.front


        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.back.val != float("inf"):
            self.back = self.back.next
        
        self.back.val = value
        self.num_nodes_avail -=1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False 

        self.front = self.front.next 
        self.num_nodes_avail += 1
        return True
        
    def Front(self) -> int:
        if not self.isEmpty():
            return self.front.val
        return -1
        

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.back.val
        return -1
        

    def isEmpty(self) -> bool:
        return self.num_nodes_avail == self.total_nodes
        

    def isFull(self) -> bool:
        return not self.num_nodes_avail
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()