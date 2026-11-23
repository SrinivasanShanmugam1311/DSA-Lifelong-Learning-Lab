# STEP-BY-STEP LOGIC
# Keep a half-open search range: low is included, high is excluded.
# Initially high equals the array length, not the last index.
# Choose the middle index.
# If its value is smaller than target, all positions through mid are too small. Move low to mid + 1.
# Otherwise keep mid as a possible first match by setting high to mid.
# When low equals high, check that the index exists and the value equals target. Otherwise return -1.
# Original implementation follows.

# Binary Search
# Find the first value at least target. Check whether it equals target.
# O(log n) time, O(1) space
def solve(a,target):
    low,high=0,len(a)
    while low<high:
        mid=low+(high-low)//2
        if a[mid] < target: low=mid+1
        else: high=mid
    return low if low < len(a) and a[low] == target else -1
