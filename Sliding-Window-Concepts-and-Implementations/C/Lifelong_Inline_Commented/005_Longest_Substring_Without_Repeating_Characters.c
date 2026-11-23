// STEP-BY-STEP LOGIC
// left marks the start of a window without duplicates.
// right reads one new character at a time.
// Remember the most recent index of each character. An unseen character has index -1.
// If the previous occurrence is inside the window, move left just past it. Never move left backward.
// Record the new last index and compute right - left + 1.
// Keep the largest valid length.
// Original implementation follows.

// Longest Substring Without Repeating Characters
// Remember the last index of each character. If it is inside the window, move left past it. Update the longest length. ASCII input.
// O(n) time, O(1) space for fixed alphabet
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
int solve(const char *s) {
    int last[256],left=0,best=0;
    for(int i=0;i<256;i++) last[i]=-1;
    for(int right=0;s[right];right++) {
        unsigned char ch=s[right];
        if(last[ch]>=left) left=last[ch]+1;
        last[ch]=right;
        if(right-left+1>best) best=right-left+1;
    }
    return best;
}
