class Node:
    def __init__(self, key, val) -> None:
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.hm = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.hm:
            self._move_to_head(self.hm[key])
            return self.hm[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.hm[key].val = value
            self._move_to_head(self.hm[key])
            return

        self.hm[key] = Node(key, value)
        self._move_to_head(self.hm[key])

        if len(self.hm) > self.cap:
            self._evict()
        
    def _move_to_head(self, node: Node):
        if node == self.tail:
            self.tail = self.tail.prev
        elif node == self.head:
            return
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        if self.head:
            self.head.prev = node
        node.prev = None
        node.next = self.head
        self.head = node

        if not self.tail:
            self.tail = self.head
    
    def _evict(self):
        print(self.tail.key, self.tail.val)
        del self.hm[self.tail.key]
        self.tail = self.tail.prev


        
