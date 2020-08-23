"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# import sys
#
# sys.path.append('../doubly_linked_list')
# from doubly_linked_list import DoublyLinkedList
#
#
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = DoublyLinkedList()
#
#     def __len__(self):
#         return self.storage.length
#
#     def enqueue(self, value):
#         self.storage.add_to_tail(value)
#
#     def dequeue(self):
#         return self.storage.remove_from_head()

# SLL Version
# import sys
#
# sys.path.append('../singly_linked_list')
# from singly_linked_list import LinkedList
#
#
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
#
#     def __len__(self):
#         return self.storage.length
#
#     def enqueue(self, value):
#         self.storage.add_to_tail(value)
#
#     def dequeue(self):
#         return self.storage.remove_head()
