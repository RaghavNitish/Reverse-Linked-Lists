# =============================================================================
# Data Structures and Algorithms Nanodegree Udacity (Linked Lists Challenges)
# 
# Problem Statement:
# Given a singly linked list, return another linked list that is the reverse of the first.
# =============================================================================

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])
    
# TODO: Complete this function to reverse linked lists here
def reverse(linked_list):
    lst = []
    reversed_linked_list = LinkedList()
    
    
    current_node = linked_list.head
    
    while current_node:
        lst.append(current_node.value)
        current_node = current_node.next
    
    for element in reversed(lst):
        reversed_linked_list.append(element)
        
    return reversed_linked_list

# =============================================================================
# #Test
# llist = LinkedList()
# for value in [4,2,5,1,-3,0]:
#     llist.append(value)
# flipped = reverse(llist)
# is_correct = list(flipped) == list([0,-3,1,5,2,4]) and list(llist) == list(reverse(flipped))
# print("Pass" if is_correct else "Fail")
# =============================================================================


