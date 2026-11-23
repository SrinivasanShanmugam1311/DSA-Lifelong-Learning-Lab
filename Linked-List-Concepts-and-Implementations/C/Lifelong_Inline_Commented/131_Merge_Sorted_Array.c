/*
Merge Sorted Array
Merge two sorted arrays into the first array, which has m+n slots.
Fill from the end so that we never overwrite an unread number.
Time O(m+n), extra space O(1).
*/

void solve(int *nums1, int m, const int *nums2, int n)
{
    int left = m - 1;
    int right = n - 1;
    int write = m + n - 1;
    while (right >= 0) {
        /* Put the largest unread number in the last free slot. */
        if (left >= 0 && nums1[left] > nums2[right]) {
            nums1[write] = nums1[left];
            left--;
        } else {
            nums1[write] = nums2[right];
            right--;
        }
        write--;
    }
    /* Remaining nums1 numbers are already in place. */
}
