/*
Minimum Size Subarray Sum
Find the shortest contiguous range with sum at least target. All numbers are positive.
Grow until valid, then shrink while valid. Positivity makes shrinking safe.
Time O(n), extra space O(1).
*/

int solve(const int *nums, int n, int target)
{
    int left = 0;
    long long window_sum = 0;
    int best = n + 1;
    for (int right = 0; right < n; right++) {
        /* Include the new rightmost number. */
        window_sum += nums[right];
        while (window_sum >= target) {
            /* Remember this valid window before shrinking. */
            int length = right - left + 1;
            if (length < best) best = length;
            /* Remove the first number to try a shorter window. */
            window_sum -= nums[left];
            left++;
        }
    }
    return best <= n ? best : 0;
}
