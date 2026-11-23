// STEP-BY-STEP LOGIC
// Start both pointers at the head.
// Before moving fast, check that fast and its next node exist.
// Move slow one link and fast two links.
// If the pointers refer to the same node after moving, a cycle exists.
// If fast reaches the end, the list has no cycle.
// Original implementation follows.

// Linked List Cycle
// Slow moves one step. Fast moves two steps. If they meet, a cycle exists. If fast reaches the end, there is no cycle.
// O(n) time, O(1) space
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
typedef struct Node { int val; struct Node *next; } Node;
bool solve(Node *head) {
    Node *slow=head,*fast=head;
    while(fast && fast->next) {
        slow=slow->next;fast=fast->next->next;
        if(slow==fast) return true;
    }
    return false;
}
