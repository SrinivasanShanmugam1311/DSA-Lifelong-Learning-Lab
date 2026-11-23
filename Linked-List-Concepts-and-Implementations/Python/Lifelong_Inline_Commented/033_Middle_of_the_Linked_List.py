# STEP-BY-STEP LOGIC
# Start slow and fast at the head.
# Move slow one link whenever fast can move two links.
# Fast covers twice the distance of slow.
# When fast reaches the end or cannot move two links, slow is at the middle.
# For an even number of nodes this returns the second middle. For an empty list it returns an empty pointer.
# Original implementation follows.

# Middle of the Linked List
# Slow moves one step. Fast moves two. When fast reaches the end, slow is at the middle (second middle for even length).
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
    return slow
