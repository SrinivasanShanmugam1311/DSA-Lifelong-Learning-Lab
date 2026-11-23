// STEP-BY-STEP LOGIC
// Keep the largest wall seen from each side, initially zero.
// Process the side with the smaller known maximum. A wall on the other side is already high enough to support that level.
// If the current wall is taller than its known maximum, update that maximum.
// Subtract the current height from the updated maximum. This is the water above the current position, possibly zero.
// Move only the processed pointer. Each position contributes once.
// Return the sum of these individual water amounts.
// Original implementation follows.

// Trapping Rain Water
// Track the highest wall seen from each side. Process the side with the smaller known maximum. Its water level is already determined.
// O(n) time, O(1) space
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
long long solve(int *a,int n) {
    int left=0,right=n-1,lm=0,rm=0;
    long long water=0;
    while(left<=right) {
        if(lm<=rm) {
            if(a[left]>lm) lm=a[left];
            water+=lm-a[left++];
        } else {
            if(a[right]>rm) rm=a[right];
            water+=rm-a[right--];
        }
    }
    return water;
}
