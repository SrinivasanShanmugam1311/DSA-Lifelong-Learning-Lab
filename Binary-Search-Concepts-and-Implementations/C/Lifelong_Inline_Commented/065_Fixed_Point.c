// STEP-BY-STEP LOGIC
// The array contains distinct sorted integers.
// Because successive values increase by at least one, value minus index never decreases.
// If a[mid] is smaller than mid, every earlier difference is negative too. Move low right.
// Otherwise keep mid as a possible first nonnegative difference.
// At the end, check that the index exists and a[low] equals low. Return -1 if not.
// Original implementation follows.

// Fixed Point
// For distinct sorted integers, a[i]-i cannot decrease. Search for zero.
// O(log n) time, O(1) space
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
int solve(int *a,int n) {
    int low=0,high=n;
    while(low<high) {
        int mid=low+(high-low)/2;
        if(a[mid]<mid) low=mid+1; else high=mid;
    }
    return low<n && a[low]==low ? low : -1;
}
