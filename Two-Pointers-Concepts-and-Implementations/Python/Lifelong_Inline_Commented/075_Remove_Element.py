# Remove Element
# O(n) time; O(1) extra space. [3,2,2,3], target 3 gives length 2 and prefix [2,2]. Inherits read/write logic from #1.
def solve(nums, target):
    # write is the next place for a value we want to keep.
    write = 0
    for read in range(len(nums)):
        # Keep values that are different from the unwanted target.
        if nums[read] != target:
            nums[write] = nums[read]
            write += 1
    # Only the first write values are part of the answer.
    return write
