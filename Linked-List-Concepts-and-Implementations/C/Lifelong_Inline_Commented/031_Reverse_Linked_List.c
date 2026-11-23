// STEP-BY-STEP LOGIC
// previous starts empty because the original first node will become the tail.
// current starts at the head.
// Save current.next before changing it, or the remaining list would be lost.
// Point current.next backward to previous.
// Move previous to current, then move current to the saved next node.
// When current is empty, previous is the new head.
// Original implementation follows.

// Reverse Linked List
// Save next before changing the link. Point current backward. Move previous and current forward.
// O(n) time, O(1) space
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
typedef struct Node { int val; struct Node *next; } Node;
Node *solve(Node *head) {
    Node *previous=NULL,*current=head;
    while(current) {
        Node *next_node=current->next;
        current->next=previous;
        previous=current;
        current=next_node;
    }
    return previous;
}
