/* Remove Duplicates II
 * O(n) time; O(1) extra space. [1,1,1,2,2,3] gives length 5 and prefix [1,1,2,2,3]. Inherits read/write logic from #1.
 */
int solve(int nums[], int n) {
    /* The input is sorted. Equal values are next to each other. */
    int write = 0;
    for (int read = 0; read < n; read++) {
        /* Accept the first two values. After that, compare with
         * the value two accepted positions back. A match means
         * we already kept two copies. */
        if (write < 2 || nums[read] != nums[write - 2]) {
            nums[write] = nums[read];
            write++;
        }
    }
    return write;
}
