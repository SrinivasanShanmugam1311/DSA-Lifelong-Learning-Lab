
# ============================================================
# Problem: Remove Duplicates from Sorted Array
# LeetCode: 26
# Pattern: Two Pointers - Slow and Fast (Same Direction)
# ============================================================
#
# PROBLEM STATEMENT:
# Remove duplicates from a sorted array in-place.
# Keep only one occurrence of each number.
# Return the number of unique elements.
#
# Example:
# Input:  [1, 1, 2, 2, 3, 3]
# Output: [1, 2, 3, _, _, _]
# Return: 3
#
# KEY OBSERVATION:
# Since the array is sorted, duplicate elements are
# always grouped together.
#
# Once we reach a new number, the previous smaller
# numbers will never appear again in the remaining input.
#
# Therefore, comparing the current element with the
# last accepted unique element is sufficient.
#
# MENTAL MAPPING:
# Slow = Tortoise
# Fast = Rabbit
#
# Slow remembers the last accepted unique element.
# Fast examines every remaining element.
#
# GOLDEN RULE:
# Fast discovers. Slow remembers.
#
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)
# ============================================================


def solve(nums):

    # Step 1: Find the total number of elements.
    n = len(nums)

    # Step 2: Handle an empty array.
    # If there are no elements, there are no unique elements.
    if n == 0:
        return 0

    # Step 3: Accept the first element automatically.
    #
    # The first element cannot be a duplicate of any
    # previously visited element.
    #
    # Slow remembers the last accepted unique element.
    slow = 0

    # Step 4: Start searching from the second element.
    #
    # The first element is already accepted.
    # Therefore, fast starts from index 1.
    fast = 1

    # Step 5: Examine every remaining element.
    #
    # Stop when fast reaches the end of the array.
    while fast < n:

        # Get the current element discovered by fast.
        current_element = nums[fast]

        # Get the last accepted unique element
        # remembered by slow.
        last_unique_element = nums[slow]

        # Step 6: POSITIVE ACCEPTANCE CONDITION.
        #
        # Have we discovered a new unique element?
        #
        # If the current element is different from the
        # last accepted element, we must accept it.
        if current_element != last_unique_element:

            # YES: We found a new unique element.
            #
            # Slow currently points to an element that
            # we have already accepted.
            #
            # We must not overwrite that element.
            #
            # Therefore, move slow to the next available
            # position before copying the new element.
            slow += 1

            # Store the newly discovered unique element.
            #
            # This brings all accepted unique elements
            # together at the beginning of the array.
            nums[slow] = current_element

        # If the condition is False:
        #
        # The current element is a duplicate.
        # Slow remains unchanged.
        # No copying is required.

        # Step 7: Always move fast.
        #
        # Whether the current element is accepted or
        # skipped, we have finished examining it.
        #
        # Continue searching for the next unique element.
        fast += 1

    # Step 8: Return the number of unique elements.
    #
    # Slow represents the last accepted INDEX,
    # not the total number of unique elements.
    #
    # Example:
    # slow = 2
    # Accepted elements = [1, 2, 3]
    # Unique count = 2 + 1 = 3
    return slow + 1


# ============================================================
# TEST CASES
# ============================================================

if __name__ == "__main__":

    test_cases = [
        ([1, 1, 2, 2, 3, 3], [1, 2, 3]),
        ([1, 1, 2], [1, 2]),
        ([1, 1, 1, 1], [1]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([1], [1]),
        ([], []),
        ([-2, -2, -1, 0, 0], [-2, -1, 0]),
    ]

    for nums, expected in test_cases:

        # Preserve the input for displaying the test result.
        original_nums = nums.copy()

        unique_count = solve(nums)

        # Only the first unique_count elements matter.
        result = nums[:unique_count]

        assert unique_count == len(expected)
        assert result == expected

        print("Input        :", original_nums)
        print("Unique count :", unique_count)
        print("Output       :", result)
        print("Status       : PASS")
        print()
