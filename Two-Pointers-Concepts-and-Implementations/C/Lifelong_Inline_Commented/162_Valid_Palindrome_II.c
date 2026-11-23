/*
Valid Palindrome II
Can the string become a palindrome after deleting at most one character?
At the first mismatch only deleting one of the two mismatched characters can help.
Time O(n), extra space O(1).
*/

#include <stdbool.h>
#include <string.h>
static bool is_palindrome(const char *text, int left, int right)
{
    while (left < right) {
        if (text[left] != text[right]) return false;
        left++;
        right--;
    }
    return true;
}
bool solve(const char *text)
{
    int left = 0;
    int right = (int)strlen(text) - 1;
    while (left < right) {
        if (text[left] != text[right]) {
            /* Try deleting either mismatched character. No further deletions. */
            return is_palindrome(text, left + 1, right) ||
                   is_palindrome(text, left, right - 1);
        }
        /* Matching characters can remain. */
        left++;
        right--;
    }
    return true;
}
