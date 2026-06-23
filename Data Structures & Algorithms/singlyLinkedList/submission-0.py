class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        curr = self.head
        i = 0
        while curr is not None:
            if i == index:
                return curr.val
            curr = curr.next
            i = i + 1
        return -1
        

    def insertHead(self, val: int) -> None:
        new_head = Node(val)
        if self.head:
            new_head.next = self.head
        if self.tail is None:
            self.tail = new_head
        self.head = new_head
        

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if self.tail is None:
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        if self.head is None:
            self.head = new_node
        

    def remove(self, index: int) -> bool:
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        curr = self.head
        i = 0

        while curr is not None:
            if i == index:
                prev.next = curr.next
                if curr.next is None:  # letzter Node entfernt
                    self.tail = prev if prev != dummy else None
                self.head = dummy.next
                return True
            prev = curr
            curr = curr.next
            i += 1

        return False

        
    def getValues(self) -> List[int]:
        if self.head is None:
            return []
        values = []
        curr = self.head
        while curr is not None:
            values.append(curr.val)
            curr = curr.next
        return values

        

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None