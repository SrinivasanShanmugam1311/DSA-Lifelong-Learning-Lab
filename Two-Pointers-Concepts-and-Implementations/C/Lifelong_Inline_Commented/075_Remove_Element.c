/* Remove Element
 * O(n) time; O(1) extra space. [3,2,2,3], target 3 gives length 2 and prefix [2,2]. Inherits read/write logic from #1.
 */
int solve(int nums[], int n, int target) {
    /* write is the next place for a value we want to keep. */
    int write = 0;
    for (int read = 0; read < n; read++) {
        /* Keep values that are different from the unwanted target. */
        if (nums[read] != target) {
            nums[write] = nums[read];
            write++;
        }
    }
    return write;
}
