# STEP-BY-STEP LOGIC
# previous starts empty because the original first node will become the tail.
# current starts at the head.
# Save current.next before changing it, or the remaining list would be lost.
# Point current.next backward to previous.
# Move previous to current, then move current to the saved next node.
# When current is empty, previous is the new head.
# Original implementation follows.

# Reverse Linked List
# Save next before changing the link. Point current backward. Move previous and current forward.
# O(n) time, O(1) space
class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def solve(head):
    previous=None
    current=head
    while current:
        next_node=current.next
        current.next=previous
        previous=current
        current=next_node
    return previous
