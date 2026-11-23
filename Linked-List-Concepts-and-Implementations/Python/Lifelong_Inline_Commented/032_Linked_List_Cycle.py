# STEP-BY-STEP LOGIC
# Start both pointers at the head.
# Before moving fast, check that fast and its next node exist.
# Move slow one link and fast two links.
# If the pointers refer to the same node after moving, a cycle exists.
# If fast reaches the end, the list has no cycle.
# Original implementation follows.

# Linked List Cycle
# Slow moves one step. Fast moves two steps. If they meet, a cycle exists. If fast reaches the end, there is no cycle.
# O(n) time, O(1) space
class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def solve(head):
    slow=fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow is fast: return True
    return False
