// STEP-BY-STEP LOGIC
// Use 26 counters for lowercase English letters.
// Convert each character into an index from 0 to 25.
// Add one for every letter in the first word.
// Subtract one for every letter in the second word.
// If any count is nonzero, the words contain different letter frequencies.
// If all counts are zero, the words are anagrams.
// Original implementation follows.

// Valid Anagram
// Count letters in the first string. Subtract letters in the second. Every count must end at zero. Lowercase English letters assumed.
// O(n+m) time, O(1) space
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
bool solve(const char *s,const char *t) {
    int count[26]={0};
    for(;*s;s++) count[*s-'a']++;
    for(;*t;t++) count[*t-'a']--;
    for(int i=0;i<26;i++) if(count[i]!=0) return false;
    return true;
}
