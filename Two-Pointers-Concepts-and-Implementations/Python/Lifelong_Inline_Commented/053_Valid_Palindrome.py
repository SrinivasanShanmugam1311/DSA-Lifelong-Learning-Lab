
# ============================================================
# Problem: Valid Palindrome
# LeetCode: 125
# Pattern: Two Pointers - Converging Pointers
# ============================================================
#
# PROBLEM STATEMENT:
# Determine whether a string is a palindrome.
#
# A palindrome reads the same forward and backward.
#
# Ignore all non-alphanumeric characters.
# Compare letters without considering uppercase or lowercase.
#
# Example:
# Input: "A man, a plan, a canal: Panama"
# Valid characters: "amanaplanacanalpanama"
# Output: True
#
# KEY OBSERVATION:
# We do not need to create a new string or reverse the string.
#
# We only need to compare valid characters from both ends.
#
# If the two characters match, they need no further checking.
# Move both pointers inward and compare the next pair.
#
# MENTAL MAPPING:
# Left pointer  -> Moves from left to right.
# Right pointer -> Moves from right to left.
#
# Both pointers converge towards the middle.
#
# POSITIVE LOGIC:
# 1. Are both characters valid?
# 2. Do both characters match?
# 3. Move the appropriate pointers.
#
# GOLDEN RULE:
# Compare valid characters.
# Skip invalid characters.
# Move both pointers after a successful match.
#
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)
# Assumption: ASCII input, as in LeetCode 125.
# ============================================================


def solve(s):

    # Step 1: Find the total number of characters.
    n = len(s)

    # Step 2: Initialize the converging pointers.
    #
    # Left starts from the first character.
    left = 0

    # Right starts from the last character.
    right = n - 1

    # Step 3: Continue until both pointers meet or cross.
    #
    # Once they meet or cross, all required character
    # pairs have been compared.
    while left < right:

        # Check whether the left character is valid.
        #
        # Alphanumeric means a letter or a digit.
        left_valid = s[left].isalnum()

        # Check whether the right character is valid.
        right_valid = s[right].isalnum()

        # Step 4: POSITIVE CONDITION.
        #
        # Are both characters valid?
        #
        # Compare characters only when both are valid.
        if left_valid and right_valid:

            # Convert the characters to lowercase.
            #
            # This allows us to treat 'A' and 'a'
            # as the same character.
            left_char = s[left].lower()
            right_char = s[right].lower()

            # Step 5: POSITIVE MATCH CONDITION.
            #
            # Do both valid characters match?
            if left_char == right_char:

                # YES: Both characters match.
                #
                # These two characters have been
                # successfully verified.
                #
                # They need no further checking.
                #
                # Move both pointers inward.
                left += 1
                right -= 1

            else:

                # NO: Both characters are valid,
                # but they are different.
                #
                # Even one mismatched pair is enough
                # to prove that the string is not
                # a palindrome.
                return False

        # Step 6: Is the left character valid?
        #
        # We reach this condition only when the previous
        # condition (both characters are valid) is False.
        #
        # If left is valid, right must be invalid.
        elif left_valid:

            # Preserve the valid left character.
            #
            # It has not been compared successfully yet.
            #
            # Skip only the invalid right character.
            right -= 1

        else:

            # Step 7: The left character is invalid.
            #
            # The right character may be valid or invalid.
            #
            # Skip the invalid left character.
            #
            # The right character will be examined again
            # during the next iteration, if required.
            left += 1

    # Step 8: All required character pairs have matched.
    #
    # We did not find any mismatched valid characters.
    #
    # Therefore, the string is a valid palindrome.
    #
    # Empty strings, single characters and strings
    # containing only ignored characters also return True.
    return True


# ============================================================
# TEST CASES
# ============================================================

if __name__ == "__main__":

    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("madam", True),
        ("racecar", True),
        ("Madam", True),
        ("abcba!", True),
        ("!abcba", True),
        ("!abcba?", True),
        ("hello", False),
        ("0P", False),
        ("12321", True),
        ("12345", False),
        ("a", True),
        ("", True),
        (" ", True),
        ("!@#$%", True),
    ]

    for s, expected in test_cases:

        result = solve(s)

        assert result == expected

        print("Input    :", repr(s))
        print("Expected :", expected)
        print("Result   :", result)
        print("Status   : PASS")
        print()
