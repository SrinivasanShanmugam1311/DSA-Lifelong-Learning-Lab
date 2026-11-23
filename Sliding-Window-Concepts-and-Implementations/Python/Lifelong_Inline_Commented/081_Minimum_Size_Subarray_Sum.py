# Minimum Size Subarray Sum
# Find the shortest contiguous range with sum at least target. All numbers are positive.
# Grow until valid, then shrink while valid. Positivity makes shrinking safe.
# Time O(n), extra space O(1).

def solve(nums, target):
    left = 0
    window_sum = 0
    best = len(nums) + 1
    for right in range(len(nums)):
        # Include the new rightmost number.
        window_sum += nums[right]
        while window_sum >= target:
            # This window is valid. Remember its length before shrinking.
            length = right - left + 1
            if length < best:
                best = length
            # Try a shorter window by removing its first number.
            window_sum -= nums[left]
            left += 1
    return best if best <= len(nums) else 0
