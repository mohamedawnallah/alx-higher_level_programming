#!/usr/bin/python3
"""
This program is meant to check if the linkedlist has a cycle or not
using the Fast and slower pointers coding pattern.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
               return True
        return False

    def create_cycle(self, index):
        if self.head is None:
            return
        node = self.head
        count = 0
        while node.next is not None:
            if count == index:
                cycle_node = node
            count += 1
        node = node.next
        node.next = cycle_node

    def print_list(self):
        if self.head is None:
            print("List is empty")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data, end=" ")
                current_node = current_node.next
            print()

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.create_cycle(1)
print(f"LinkedList has cycle: {linked_list.has_cycle()}")  # Output: False
