# STEP-BY-STEP LOGIC
# Use 26 counters for lowercase English letters.
# Convert each character into an index from 0 to 25.
# Add one for every letter in the first word.
# Subtract one for every letter in the second word.
# If any count is nonzero, the words contain different letter frequencies.
# If all counts are zero, the words are anagrams.
# Original implementation follows.

# Valid Anagram
# Count letters in the first string. Subtract letters in the second. Every count must end at zero. Lowercase English letters assumed.
# O(n+m) time, O(1) space
def solve(s,t):
    count=[0]*26
    for ch in s: count[ord(ch)-97]+=1
    for ch in t: count[ord(ch)-97]-=1
    return all(x==0 for x in count)
