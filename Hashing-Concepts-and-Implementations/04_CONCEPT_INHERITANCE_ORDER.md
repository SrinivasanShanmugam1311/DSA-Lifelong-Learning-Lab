# Concept inheritance — Hashing

Follow this order for learning. Original IDs stay unchanged. Adjacent problems may be different branches, not direct code reuse.

## Lesson 1: #020 Valid Anagram
Starting foundation.

Count letters in first string and subtract second; all counts must be zero.

Example: anagram,nagaram -> true
Time: O(n+m). Auxiliary space: O(alphabet).
Source status: C/Python available.

## Lesson 2: #069 Ransom Note
Previous lesson: #020 Valid Anagram

Count available letters; consume letters required by note; fail on shortage.

Example: aa,aab -> true
Time: O(n+m). Auxiliary space: O(alphabet).
Source status: Pending.

## Lesson 3: #019 Two Sum
Previous lesson: #069 Ransom Note

For each number check target minus number in map before inserting current index.

Example: 2,7,11,15 target 9 -> 0,1
Time: O(n) expected. Auxiliary space: O(n).
Source status: Pending.

## Lesson 4: #068 Group Anagrams
Previous lesson: #019 Two Sum

Use frequency tuple as canonical key for each lowercase word; append word to corresponding group.

Example: eat,tea,bat -> two groups
Time: O(total characters + 26*n) expected. Auxiliary space: O(n) auxiliary keys.
Source status: Pending.

## Lesson 5: #054 Valid Sudoku
Previous lesson: #068 Group Anagrams

Track digit presence in row, column and 3x3 box; reject repeat; skip empty cells.

Example: two 5s in one row -> false
Time: O(81). Auxiliary space: O(81) fixed board.
Source status: Pending.

## Lesson 6: #055 Set Matrix Zeroes
Previous lesson: #054 Valid Sudoku

Use first row and column as zero markers; remember whether original first row/column contains zero; clear marked cells.

Example: [[1,0],[3,4]] -> [[0,0],[3,0]]
Time: O(rows*cols). Auxiliary space: O(1).
Source status: Pending.

## Lesson 7: #070 Pairing Users by Attributes
Previous lesson: #055 Set Matrix Zeroes

Build a canonical key from attributes; keep unmatched users per key; pair compatible users according to given rules.

Example: same key A,A -> pair (illustrative)
Time: O(n*a) expected for fixed-size canonical attributes. Auxiliary space: O(n*a).
Source status: Pending.

## Lesson 8: #071 Missing Element Arbitrary Range
Previous lesson: #070 Pairing Users by Attributes

Store input values in a set; scan requested finite range for absent value.

Example: range 0..4, input 0,1,3,4 -> 2
Time: O(n+R) expected. Auxiliary space: O(n).
Source status: Pending.

## Lesson 9: #072 Missing Element Limited Memory
Previous lesson: #071 Missing Element Arbitrary Range

Count numbers per bucket; find underfull bucket; rescan with bitmap for that bucket. Requires distinct input or a stronger counting method.

Example: range 0..7, missing 5 -> bucket 4..7
Time: O(n+R/B+B) for two passes. Auxiliary space: O(R/B+B).
Source status: Pending.

## Lesson 10: #073 Majority Element
Previous lesson: #072 Missing Element Limited Memory

Maintain candidate and vote balance; cancel different values; verify candidate if majority not guaranteed.

Example: 2,2,1 -> 2
Time: O(n). Auxiliary space: O(1).
Source status: C/Python available.

## Lesson 11: #074 Frequent Items in a Stream
Previous lesson: #073 Majority Element

Maintain at most k-1 counters; on full table and new item decrement all counters; verify candidates in second pass for exact > n/k.

Example: 1,1,2,3,1 k=3 -> 1
Time: O(n) expected amortized. Auxiliary space: O(k).
Source status: Pending.

## Lesson 12: #021 Longest Consecutive Sequence
Previous lesson: #074 Frequent Items in a Stream

Build set; start counting only when predecessor absent; extend consecutive run.

Example: 100,4,200,1,3,2 -> 4
Time: O(n) expected. Auxiliary space: O(n).
Source status: Pending.

## Lesson 13: #022 Subarray Sum Equals K
Previous lesson: #021 Longest Consecutive Sequence

Keep counts of previous prefix sums; add frequency of current prefix minus k; then record current prefix.

Example: 1,1,1 k=2 -> 2
Time: O(n) expected. Auxiliary space: O(n).
Source status: Pending.
