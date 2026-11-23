// STEP-BY-STEP LOGIC
// Reuse the insertion-position search.
// The only change is that values equal to target must also be skipped.
// If a[mid] is less than or equal to target, move low to mid + 1.
// Otherwise keep mid by setting high to mid.
// Return the first strictly greater index, or -1 if none exists. This pack uses -1 rather than n.
// Original implementation follows.

// Upper Bound
// Find the first value strictly greater than target.
// O(log n) time, O(1) space
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
int solve(int *a,int n,int target) {
    int low=0,high=n;
    while(low<high) {
        int mid=low+(high-low)/2;
        if(a[mid] <= target) low=mid+1;
        else high=mid;
    }
    return low<n ? low : -1;
}
