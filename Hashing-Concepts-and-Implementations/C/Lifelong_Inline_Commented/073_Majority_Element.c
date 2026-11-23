// STEP-BY-STEP LOGIC
// Assume a majority value occurs more than half the time.
// candidate is the current possible majority. count is its unmatched vote count.
// When count is zero, choose the current value as the new candidate.
// Increase count for a matching value. Decrease it for a different value.
// Each cancellation removes two different values, so a guaranteed majority cannot be eliminated completely.
// Return the surviving candidate. Without a guaranteed majority, a second verification pass is needed.
// Original implementation follows.

// Majority Element
// Cancel two different values. A guaranteed majority survives all cancellations.
// O(n) time, O(1) space
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
int solve(int *a,int n) {
    int candidate=0,count=0;
    for(int i=0;i<n;i++) {
        if(count==0) candidate=a[i];
        if(a[i]==candidate) count++; else count--;
    }
    return candidate;
}
