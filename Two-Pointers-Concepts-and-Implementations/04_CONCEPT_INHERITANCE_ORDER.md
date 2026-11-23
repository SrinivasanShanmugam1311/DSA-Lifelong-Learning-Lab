# Concept inheritance — Two-Pointers

Follow this order for learning. Original IDs stay unchanged. Adjacent problems may be different branches, not direct code reuse.

## Lesson 1: #053 Valid Palindrome
Starting foundation.

Compare opposite characters; skip non-alphanumeric characters; move inward after a match.

Example: A man, a plan, a canal: Panama -> true
Time: O(n). Auxiliary space: O(1).
Source status: C/Python available.

## Lesson 2: #001 Remove Duplicates from Sorted Array
Previous lesson: #053 Valid Palindrome

Read each element; write only when it differs from the last accepted value.

Example: 1,1,2 -> 1,2
Time: O(n). Auxiliary space: O(1).
Source status: C/Python available.

## Lesson 3: #052 Two Sum II
Previous lesson: #001 Remove Duplicates from Sorted Array

Add the two endpoints; increase left for a small sum and decrease right for a large sum.

Example: 2,7,11 target 9 -> indices 1,2
Time: O(n). Auxiliary space: O(1).
Source status: C/Python available.

## Lesson 4: #067 Intersection of Sorted Arrays
Previous lesson: #052 Two Sum II

Compare the current elements of both sorted arrays; advance the smaller; emit a match once and advance both.

Example: 1,2,2 and 2,3 -> 2
Time: O(n+m). Auxiliary space: O(1) excluding output.
Source status: Pending.

## Lesson 5: #002 3Sum
Previous lesson: #067 Intersection of Sorted Arrays

Sort; fix one number; use left/right search for its negative; skip duplicate values.

Example: -1,0,1,2,-1,-4 -> [-1,-1,2],[-1,0,1]
Time: O(n²). Auxiliary space: sorting dependent, excluding output.
Source status: Pending.

## Lesson 6: #003 Container With Most Water
Previous lesson: #002 3Sum

Compute width times shorter height; save maximum; move the shorter wall.

Example: 1,8,6,2,5,4,8,3,7 -> 49
Time: O(n). Auxiliary space: O(1).
Source status: C/Python available.

## Lesson 7: #004 Trapping Rain Water
Previous lesson: #003 Container With Most Water

Maintain left and right maximum heights; process the side with smaller maximum; add maximum minus current height.

Example: 5,1,2,4 -> 5
Time: O(n). Auxiliary space: O(1).
Source status: C/Python available.
