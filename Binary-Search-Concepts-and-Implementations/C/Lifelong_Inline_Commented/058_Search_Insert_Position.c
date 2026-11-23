// STEP-BY-STEP LOGIC
// Reuse the half-open binary search range.
// If a[mid] is smaller than target, move low past mid.
// Otherwise keep mid as a possible insertion position by moving high to mid.
// Stop when the two boundaries meet.
// Return low even if target is absent. It is where target belongs in sorted order.
// Original implementation follows.

// Search Insert Position
// Find the first position whose value is at least target.
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
        if(a[mid] < target) low=mid+1;
        else high=mid;
    }
    return low;
}
