# Concept inheritance — Binary-Search

Follow this order for learning. Original IDs stay unchanged. Adjacent problems may be different branches, not direct code reuse.

## Lesson 1: #062 Binary Search
Starting foundation.

Compare middle with target; discard the impossible half.

Example: 1,3,5 target 3 -> 1
Time: O(log n). Auxiliary space: O(1).
Source status: C/Python available.

## Lesson 2: #058 Search Insert Position
Previous lesson: #062 Binary Search

Find the first index whose value is at least target using a half-open interval.

Example: 1,3,5,6 target 2 -> 1
Time: O(log n). Auxiliary space: O(1).
Source status: C/Python available.

## Lesson 3: #064 Upper Bound
Previous lesson: #058 Search Insert Position

Change lower-bound comparison to find first value strictly greater than target.

Example: 1,2,2,4 target 2 -> 3
Time: O(log n). Auxiliary space: O(1).
Source status: C/Python available.

## Lesson 4: #059 Find First and Last Position
Previous lesson: #064 Upper Bound

Find lower and upper bounds; verify target exists; return lower and upper minus one.

Example: 5,7,7,8,8,10 target 8 -> 3,4
Time: O(log n). Auxiliary space: O(1).
Source status: Pending.

## Lesson 5: #065 Fixed Point
Previous lesson: #059 Find First and Last Position

For distinct sorted integers, compare value with index; search first index where value minus index is nonnegative; verify equality.

Example: -1,0,2,4 -> 2
Time: O(log n). Auxiliary space: O(1).
Source status: C/Python available.

## Lesson 6: #013 Search a 2D Matrix
Previous lesson: #065 Fixed Point

Treat globally sorted matrix as one array; convert middle to row and column using division and remainder.

Example: [[1,3],[5,7]],5 -> true
Time: O(log(rows*cols)). Auxiliary space: O(1).
Source status: Pending.

## Lesson 7: #011 Search in Rotated Sorted Array
Previous lesson: #013 Search a 2D Matrix

Identify sorted half; check if target lies inside it; discard the other half.

Example: 4,5,6,7,0,1,2 target 0 -> 4
Time: O(log n) distinct values. Auxiliary space: O(1).
Source status: Pending.

## Lesson 8: #012 Find Minimum in Rotated Sorted Array
Previous lesson: #011 Search in Rotated Sorted Array

Compare middle with rightmost value; minimum is in right half if middle is greater, otherwise keep middle and left half.

Example: 3,4,5,1,2 -> 1
Time: O(log n) distinct values. Auxiliary space: O(1).
Source status: C/Python available.

## Lesson 9: #015 Time Based Key-Value Store
Previous lesson: #012 Find Minimum in Rotated Sorted Array

Store increasing timestamp/value pairs per key; upper-bound search timestamps and return previous value.

Example: set a=x at 1, get a at 3 -> x
Time: O(log k) lookup, amortized O(1) append expected. Auxiliary space: O(total entries).
Source status: Pending.

## Lesson 10: #066 Search Unknown Length Array
Previous lesson: #015 Time Based Key-Value Store

Double the search bound until reader value reaches target or sentinel; binary search the bracket.

Example: target at index 20 -> 20
Time: O(log(i+2)). Auxiliary space: O(1).
Source status: Pending.

## Lesson 11: #063 Computing Square Roots
Previous lesson: #066 Search Unknown Length Array

Search largest integer whose square is at most x; use wide arithmetic or division.

Example: 27 -> 5
Time: O(log(x+1)). Auxiliary space: O(1).
Source status: C/Python available.

## Lesson 12: #060 Cutting Wood
Previous lesson: #063 Computing Square Roots

At candidate height sum wood above height; if enough, save height and try higher.

Example: 20,15,10,17 need 7 -> 15
Time: O(n log(H+1)). Auxiliary space: O(1).
Source status: Pending.

## Lesson 13: #014 Koko Eating Bananas
Previous lesson: #060 Cutting Wood

At candidate speed sum ceiling divisions; if hours fit, try smaller speed.

Example: 3,6,7,11 h=8 -> 4
Time: O(n log M). Auxiliary space: O(1).
Source status: Pending.

## Lesson 14: #016 Magnetic Force Between Two Balls
Previous lesson: #014 Koko Eating Bananas

Sort positions; greedily place balls at least candidate distance apart; if enough fit, try larger distance.

Example: 1,2,3,4,7 m=3 -> 3
Time: O(n log n + n log R). Auxiliary space: sorting dependent.
Source status: Pending.

## Lesson 15: #017 Split Array Largest Sum
Previous lesson: #016 Magnetic Force Between Two Balls

For candidate sum limit greedily start a new partition when adding next nonnegative value exceeds limit; minimize feasible limit.

Example: 7,2,5,10,8 k=2 -> 18
Time: O(n log(sum+1)). Auxiliary space: O(1).
Source status: Pending.

## Lesson 16: #018 Median of Two Sorted Arrays
Previous lesson: #017 Split Array Largest Sum

Partition smaller sorted array; derive complementary partition; move until both left boundaries are <= opposite right boundaries.

Example: 1,3 and 2 -> 2
Time: O(log(min(m,n)+1)). Auxiliary space: O(1).
Source status: Pending.
