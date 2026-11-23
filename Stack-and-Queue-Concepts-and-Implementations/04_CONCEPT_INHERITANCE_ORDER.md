# Concept inheritance — Stack-and-Queue

Follow this order for learning. Original IDs stay unchanged. Adjacent problems may be different branches, not direct code reuse.

## Lesson 1: #023 Valid Parentheses
Starting foundation.

Push opening brackets; for closing bracket check matching top; accept only empty stack at end.

Example: ([]) -> true
Time: O(n). Auxiliary space: O(n).
Source status: C/Python available.

## Lesson 2: #025 Implement Queue Using Stacks
Previous lesson: #023 Valid Parentheses

Push into input stack; transfer to output stack only when output empty; pop output top.

Example: push 1,2; pop -> 1
Time: O(1) amortized per operation. Auxiliary space: O(n).
Source status: Pending.

## Lesson 3: #026 Min Stack
Previous lesson: #025 Implement Queue Using Stacks

Store running minimum with each pushed item; pop value and its minimum together.

Example: push 3,1,2; min -> 1
Time: O(1) per operation. Auxiliary space: O(n).
Source status: Pending.

## Lesson 4: #027 Evaluate Reverse Polish Notation
Previous lesson: #026 Min Stack

Push numbers; for operator pop right then left; evaluate and push result; truncate division toward zero.

Example: 2,1,+,3,* -> 9
Time: O(n). Auxiliary space: O(n).
Source status: Pending.

## Lesson 5: #061 Basic Calculator
Previous lesson: #027 Evaluate Reverse Polish Notation

Track current total and sign; on opening parenthesis save outer total and sign; on closing combine inner result.

Example: 1-(2-3) -> 2
Time: O(n). Auxiliary space: O(n).
Source status: Pending.

## Lesson 6: #024 Next Greater Element I
Previous lesson: #061 Basic Calculator

Use decreasing stack; when larger value arrives resolve smaller pending values; map value to next greater.

Example: [4,1,2] in [1,3,4,2] -> -1,3,-1
Time: O(n+m) expected. Auxiliary space: O(n).
Source status: Pending.

## Lesson 7: #028 Daily Temperatures
Previous lesson: #024 Next Greater Element I

Store unresolved day indices; pop colder days when warmer day arrives; record index difference.

Example: 73,74,75 -> 1,1,0
Time: O(n). Auxiliary space: O(n).
Source status: Pending.

## Lesson 8: #029 Car Fleet
Previous lesson: #028 Daily Temperatures

Sort cars by position descending; compute arrival time; count new fleet only when arrival exceeds front fleet time.

Example: target 12 positions 10,8 speeds 2,4 -> 1
Time: O(n log n). Auxiliary space: O(n) sorting dependent.
Source status: Pending.

## Lesson 9: #030 Largest Rectangle in Histogram
Previous lesson: #029 Car Fleet

Maintain increasing bar indices; when shorter bar arrives pop and compute width using new top; flush at end.

Example: 2,1,5,6,2,3 -> 10
Time: O(n). Auxiliary space: O(n).
Source status: Pending.
