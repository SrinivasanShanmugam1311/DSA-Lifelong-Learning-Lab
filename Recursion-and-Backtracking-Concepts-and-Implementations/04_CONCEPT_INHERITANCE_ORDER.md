# Concept inheritance — Recursion-and-Backtracking

Follow this order for learning. Original IDs stay unchanged. Adjacent problems may be different branches, not direct code reuse.

## Lesson 1: #049 Subsets
Starting foundation.

Record current path; choose each remaining item; recurse with next index; undo choice.

Example: 1,2 -> [],[1],[1,2],[2]
Time: O(n*2^n) including output. Auxiliary space: O(n) excluding output.
Source status: C/Python available.

## Lesson 2: #046 Combinations
Previous lesson: #049 Subsets

Choose increasing numbers; record only when path length k; prune when remaining numbers cannot fill path.

Example: n=3 k=2 -> 12,13,23
Time: O(k*C(n,k)) output-sensitive with pruning. Auxiliary space: O(k).
Source status: Pending.

## Lesson 3: #045 Combination Sum
Previous lesson: #046 Combinations

Choose positive candidate; recurse with same index to allow reuse; subtract from remaining target; record at zero.

Example: 2,3,6,7 target 7 -> [2,2,3],[7]
Time: exponential, output dependent. Auxiliary space: O(target/min candidate).
Source status: Pending.

## Lesson 4: #050 Combination Sum II
Previous lesson: #045 Combination Sum

Sort candidates; skip equal choices at same depth; recurse with next index to forbid reuse.

Example: 1,1,2 target 2 -> [1,1],[2]
Time: O(n*2^n) upper bound. Auxiliary space: O(n).
Source status: Pending.

## Lesson 5: #051 Combination Sum III
Previous lesson: #050 Combination Sum II

Choose increasing digits 1..9; require both k choices and remaining sum zero; prune impossible branches.

Example: k=3 n=7 -> [1,2,4]
Time: O(2^9 * k) upper bound. Auxiliary space: O(k).
Source status: Pending.

## Lesson 6: #047 Permutations
Previous lesson: #051 Combination Sum III

Choose any unused element; mark used; recurse; unmark; record full path.

Example: 1,2 -> 12,21
Time: O(n*n!). Auxiliary space: O(n).
Source status: Pending.

## Lesson 7: #048 Permutations II
Previous lesson: #047 Permutations

Sort; skip equal unused predecessor at same depth; otherwise use permutation template.

Example: 1,1,2 -> 112,121,211
Time: O(n*n!) upper bound. Auxiliary space: O(n).
Source status: Pending.
