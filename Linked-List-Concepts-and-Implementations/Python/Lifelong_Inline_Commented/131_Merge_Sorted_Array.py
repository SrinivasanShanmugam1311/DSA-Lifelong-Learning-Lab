# Merge Sorted Array
# Merge two sorted arrays into the first array, which has m+n slots.
# Fill from the end so that we never overwrite an unread number.
# Time O(m+n), extra space O(1).

def solve(nums1, m, nums2, n):
    left = m - 1
    right = n - 1
    write = m + n - 1
    while right >= 0:
        # The largest unread number belongs at the last free position.
        if left >= 0 and nums1[left] > nums2[right]:
            nums1[write] = nums1[left]
            left -= 1
        else:
            nums1[write] = nums2[right]
            right -= 1
        write -= 1
    # Any remaining numbers in nums1 are already in place.
    return nums1
