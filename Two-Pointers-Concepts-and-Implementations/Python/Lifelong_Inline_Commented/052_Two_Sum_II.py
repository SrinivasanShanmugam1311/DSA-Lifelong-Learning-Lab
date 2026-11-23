# STEP-BY-STEP LOGIC
# The input must already be sorted.
# Start with the smallest and largest available values.
# If their sum equals target, return their one-based positions.
# If the sum is too small, even the largest available partner cannot help the left value. Move left forward.
# If the sum is too large, even the smallest available partner cannot help the right value. Move right backward.
# Stop when the pointers meet; a pair requires two different positions.
# Original implementation follows.

# Two Sum II
# Compare the sum of the two ends with target. Move left to increase the sum. Move right to decrease it. Return one-based indices.
# O(n) time, O(1) extra space
def solve(a,target):
    left,right=0,len(a)-1
    while left<right:
        total=a[left]+a[right]
        if total==target: return [left+1,right+1]
        if total<target: left+=1
        else: right-=1
    return []
