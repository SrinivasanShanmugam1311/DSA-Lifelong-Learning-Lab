// STEP-BY-STEP LOGIC
// Search possible integer square roots rather than array elements.
// A candidate is valid when its square is no larger than x.
// For a valid candidate, search larger values by moving low to mid + 1.
// For an invalid candidate, move high to mid - 1.
// When the search ends, high is the largest valid integer.
// C uses x / mid to avoid multiplication overflow and starts at 1 to avoid division by zero. Python can multiply safely and starts at 0.
// Original implementation follows.

// Computing Square Roots
// Search for the greatest integer whose square is at most x. Use division in C to avoid overflow.
// O(log x) time, O(1) space
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
int solve(int x) {
    int low=1,high=x;
    while(low<=high) {
        int mid=low+(high-low)/2;
        if(mid<=x/mid) low=mid+1;
        else high=mid-1;
    }
    return high;
}
