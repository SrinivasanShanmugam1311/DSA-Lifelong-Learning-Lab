# STEP-BY-STEP LOGIC
# The rotated array contains distinct values and is nonempty.
# Compare the middle value with the rightmost value.
# If middle is greater, the rotation minimum must lie strictly to its right.
# Otherwise the minimum is at middle or somewhere to its left. Keep middle.
# Stop when one candidate remains. Return its value, not its index.
# Original implementation follows.

# Find Minimum in Rotated Sorted Array
# Compare middle with the right end. If middle is larger, minimum is to its right. Otherwise keep middle. Distinct elements assumed.
# O(log n) time, O(1) space
def solve(a):
    low,high=0,len(a)-1
    while low<high:
        mid=low+(high-low)//2
        if a[mid]>a[high]: low=mid+1
        else: high=mid
    return a[low]
