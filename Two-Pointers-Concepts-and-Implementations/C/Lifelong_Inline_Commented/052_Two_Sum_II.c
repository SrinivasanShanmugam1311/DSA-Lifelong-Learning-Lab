// STEP-BY-STEP LOGIC
// The input must already be sorted.
// Start with the smallest and largest available values.
// If their sum equals target, return their one-based positions.
// If the sum is too small, even the largest available partner cannot help the left value. Move left forward.
// If the sum is too large, even the smallest available partner cannot help the right value. Move right backward.
// Stop when the pointers meet; a pair requires two different positions.
// Original implementation follows.

// Two Sum II
// Compare the sum of the two ends with target. Move left to increase the sum. Move right to decrease it. Return one-based indices.
// O(n) time, O(1) extra space
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
bool solve(int *a,int n,int target,int out[2]) {
    int left=0,right=n-1;
    while(left<right) {
        long long total=(long long)a[left]+a[right];
        if(total==target) {out[0]=left+1;out[1]=right+1;return true;}
        if(total<target) left++; else right--;
    }
    return false;
}
