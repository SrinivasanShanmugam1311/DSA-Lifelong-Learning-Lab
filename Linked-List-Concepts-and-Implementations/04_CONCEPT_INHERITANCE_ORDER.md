# Concept inheritance — Linked-List

Follow this order for learning. Original IDs stay unchanged. Adjacent problems may be different branches, not direct code reuse.

## Lesson 1: #031 Reverse Linked List
Starting foundation.

Save next; point current to previous; advance previous and current.

Example: 1->2->3 becomes 3->2->1
Time: O(n). Auxiliary space: O(1).
Source status: C/Python available.

## Lesson 2: #033 Middle of the Linked List
Previous lesson: #031 Reverse Linked List

Move slow one step and fast two; slow reaches middle when fast reaches end.

Example: 1->2->3 -> 2
Time: O(n). Auxiliary space: O(1).
Source status: C/Python available.

## Lesson 3: #032 Linked List Cycle
Previous lesson: #033 Middle of the Linked List

Move slow one step and fast two; meeting means cycle; null fast means no cycle.

Example: tail points to head -> true
Time: O(n). Auxiliary space: O(1).
Source status: C/Python available.

## Lesson 4: #056 Happy Number
Previous lesson: #032 Linked List Cycle

Replace next pointer by sum of squared digits; use slow/fast to detect cycle or reach 1.

Example: 19 -> true
Time: O(log n) initial digit processing for fixed-base integers. Auxiliary space: O(1).
Source status: Pending.

## Lesson 5: #041 Find the Duplicate Number
Previous lesson: #056 Happy Number

Treat array values as next indices; find meeting point; reset one pointer to start and move both one step to cycle entrance.

Example: 1,3,4,2,2 -> 2
Time: O(n). Auxiliary space: O(1).
Source status: Pending.

## Lesson 6: #034 Merge Two Sorted Lists
Previous lesson: #041 Find the Duplicate Number

Choose smaller head; append it to result tail; advance chosen list; attach remainder.

Example: 1,3 and 2,4 -> 1,2,3,4
Time: O(n+m). Auxiliary space: O(1).
Source status: Pending.

## Lesson 7: #036 Intersection of Two Linked Lists
Previous lesson: #034 Merge Two Sorted Lists

Walk two lists; redirect each null pointer to opposite head; stop when node identities match.

Example: shared tail node 8 -> node 8
Time: O(n+m). Auxiliary space: O(1).
Source status: Pending.

## Lesson 8: #037 Remove Nth Node From End of List
Previous lesson: #036 Intersection of Two Linked Lists

Use dummy head; advance fast n steps; move both until fast at last node; bypass slow.next.

Example: 1,2,3 n=2 -> 1,3
Time: O(n). Auxiliary space: O(1).
Source status: Pending.

## Lesson 9: #035 Palindrome Linked List
Previous lesson: #037 Remove Nth Node From End of List

Find middle; reverse second half; compare values; restore second half.

Example: 1,2,2,1 -> true
Time: O(n). Auxiliary space: O(1).
Source status: Pending.

## Lesson 10: #038 Reorder List
Previous lesson: #035 Palindrome Linked List

Split at middle; reverse second half; alternate nodes from each half.

Example: 1,2,3,4 -> 1,4,2,3
Time: O(n). Auxiliary space: O(1).
Source status: Pending.

## Lesson 11: #040 Add Two Numbers
Previous lesson: #038 Reorder List

Add current digits plus carry; append remainder modulo ten; carry is quotient; continue until no digits or carry.

Example: 2,4,3 plus 5,6,4 -> 7,0,8
Time: O(max(n,m)). Auxiliary space: O(1) excluding output.
Source status: Pending.

## Lesson 12: #039 Copy List With Random Pointer
Previous lesson: #040 Add Two Numbers

Interleave copied nodes with originals; assign random via original.random.next; separate lists and restore originals.

Example: two nodes random to each other -> independent copy
Time: O(n). Auxiliary space: O(1) excluding output.
Source status: Pending.

## Lesson 13: #042 LRU Cache
Previous lesson: #039 Copy List With Random Pointer

Use hash map to find nodes; doubly linked list tracks recency; move accessed node to front and evict tail when full.

Example: capacity 1 put 1 then 2 -> 1 evicted
Time: O(1) expected per operation. Auxiliary space: O(capacity).
Source status: Pending.

## Lesson 14: #043 Merge K Sorted Lists
Previous lesson: #042 LRU Cache

Merge lists in pairs repeatedly until one remains; reuse two-list merge.

Example: [1,4],[2,3] -> 1,2,3,4
Time: O(N log(k+1)). Auxiliary space: O(1) auxiliary if modifying input list array.
Source status: Pending.

## Lesson 15: #044 Reverse Nodes in K Group
Previous lesson: #043 Merge K Sorted Lists

Verify k nodes exist; reverse exactly k; reconnect previous group tail and remaining list; leave incomplete group intact.

Example: 1,2,3,4,5 k=2 -> 2,1,4,3,5
Time: O(n). Auxiliary space: O(1).
Source status: Pending.
