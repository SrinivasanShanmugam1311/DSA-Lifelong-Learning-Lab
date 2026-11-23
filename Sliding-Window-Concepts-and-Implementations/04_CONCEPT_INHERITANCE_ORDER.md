# Concept inheritance — Sliding-Window

Follow this order for learning. Original IDs stay unchanged. Adjacent problems may be different branches, not direct code reuse.

## Lesson 1: #005 Longest Substring Without Repeating Characters
Starting foundation.

Expand right; remember last index of each character; move left past a repeated character if it is inside the window.

Example: abcabcbb -> 3
Time: O(n). Auxiliary space: O(alphabet).
Source status: C/Python available.

## Lesson 2: #006 Fruit Into Baskets
Previous lesson: #005 Longest Substring Without Repeating Characters

Count fruit types; expand right; shrink left while more than two types remain; save maximum length.

Example: 1,2,1 -> 3
Time: O(n). Auxiliary space: O(1) for at most three types.
Source status: Pending.

## Lesson 3: #007 Longest Repeating Character Replacement
Previous lesson: #006 Fruit Into Baskets

Count letters; track highest frequency seen; shrink when length minus highest frequency exceeds k; save maximum length.

Example: AABABBA, k=1 -> 4
Time: O(n). Auxiliary space: O(alphabet).
Source status: Pending.

## Lesson 4: #008 Permutation in String
Previous lesson: #007 Longest Repeating Character Replacement

Count pattern letters; maintain a window exactly the pattern length; compare frequency arrays.

Example: ab in eidbaooo -> true
Time: O(n+m) fixed alphabet. Auxiliary space: O(alphabet).
Source status: Pending.

## Lesson 5: #057 Find All Anagrams in a String
Previous lesson: #008 Permutation in String

Reuse the fixed window frequency comparison; record each matching start instead of returning early.

Example: cbaebabacd, abc -> 0,6
Time: O(n+m) fixed alphabet. Auxiliary space: O(alphabet) excluding output.
Source status: Pending.

## Lesson 6: #009 Minimum Window Substring
Previous lesson: #057 Find All Anagrams in a String

Count required letters; expand until all requirements met; shrink while valid and remember shortest window.

Example: ADOBECODEBANC, ABC -> BANC
Time: O(n+m). Auxiliary space: O(alphabet).
Source status: Pending.

## Lesson 7: #010 Sliding Window Maximum
Previous lesson: #009 Minimum Window Substring

Keep indices in a decreasing deque; remove expired indices from front and smaller values from back; front is maximum.

Example: 1,3,-1,-3,5,3,6,7 k=3 -> 3,3,5,5,6,7
Time: O(n). Auxiliary space: O(k).
Source status: Pending.
