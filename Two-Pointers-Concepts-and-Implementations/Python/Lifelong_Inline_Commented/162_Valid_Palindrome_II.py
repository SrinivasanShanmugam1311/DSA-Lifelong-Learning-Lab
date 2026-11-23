# Valid Palindrome II
# Can the string become a palindrome after deleting at most one character?
# At the first mismatch only deleting one of the two mismatched characters can help.
# Time O(n), extra space O(1).

def is_palindrome(text, left, right):
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

def solve(text):
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            # Try deleting the left character or the right character.
            # No more deletions are allowed in either remaining range.
            return (is_palindrome(text, left + 1, right) or
                    is_palindrome(text, left, right - 1))
        # Matching characters do not need to be deleted.
        left += 1
        right -= 1
    return True
