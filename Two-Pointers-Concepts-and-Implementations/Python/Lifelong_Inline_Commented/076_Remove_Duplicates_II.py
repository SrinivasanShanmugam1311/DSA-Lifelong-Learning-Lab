# Remove Duplicates II
# O(n) time; O(1) extra space. [1,1,1,2,2,3] gives length 5 and prefix [1,1,2,2,3]. Inherits read/write logic from #1.
def solve(nums):
    # The input is sorted. Equal values are next to each other.
    write = 0
    for read in range(len(nums)):
        # The first two accepted values are always safe.
        # After that, compare with the value two accepted positions back.
        # If it matches, we already kept two copies of this value.
        if write < 2 or nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1
    return write
