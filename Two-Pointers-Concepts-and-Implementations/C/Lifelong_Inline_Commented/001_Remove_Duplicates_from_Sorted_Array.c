// STEP-BY-STEP LOGIC
// The array is sorted, so equal numbers sit together.
// write tells us where the next unique number belongs.
// read examines every original value. It never moves backward.
// If write is zero, accept the first value. Otherwise compare with the last accepted value at write - 1.
// Copy a new value and increase write. Skip a duplicate without increasing write.
// Return write, not the entire array. Only the first write entries are the answer.
// Original implementation follows.

// Remove Duplicates from Sorted Array
// Keep a write position. Copy each new value there. The sorted order puts duplicates together.
// O(n) time, O(1) extra space
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
int solve(int *a, int n) {
    int write = 0;
    for (int read = 0; read < n; read++) {
        if (write == 0 || a[read] != a[write-1])
            a[write++] = a[read];
    }
    return write;
}
