class Node: 
    def __init__(self,key=None,value=None):
        self.prev = self.next= None
        self.key,self.value= key,value

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.prev = self.tail 
        self.tail.next = self.head
        self.hashm = {}
        self.capacity = capacity
        self.cur = 0

    def get(self, key: int) -> int:
        res = -1
        if key in self.hashm: 
            node = self.hashm[key]
            res = node.value
            node.next.prev, node.prev.next = node.prev, node.next
            node.prev, self.head.prev.next = self.head.prev,node
            node.next, self.head.prev = self.head, node
        return res

    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.hashm: 
            node = self.hashm[key]
            node.value = value
            node.next.prev, node.prev.next = node.prev, node.next
        else: 
            node = Node(key,value)
            self.hashm[node.key] = node
            self.cur +=1
        node.prev, self.head.prev.next = self.head.prev,node
        node.next, self.head.prev = self.head,node
        if self.cur > self.capacity:
            del self.hashm[self.tail.next.key]
            self.tail.next = self.tail.next.next
            self.tail.next.prev = self.tail
            self.cur -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)