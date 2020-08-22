class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.length = 0

    def __str__(self):
        pass


