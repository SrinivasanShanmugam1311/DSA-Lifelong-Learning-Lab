// STEP-BY-STEP LOGIC
// Start with one pointer at each end.
// Skip punctuation on either side. It is not part of the comparison.
// Convert the two remaining characters to lowercase before comparing.
// If they differ, the string cannot be a palindrome.
// If they match, move both pointers inward. Those characters need no further checking.
// When the pointers meet or cross, every required pair has matched.
// Original implementation follows.

// Valid Palindrome
// Skip punctuation at both ends. Compare lowercase letters or digits. Move inward after a match.
// O(n) time, O(1) space (ASCII input)
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
bool solve(const char *s) {
    int left=0,right=(int)strlen(s)-1;
    while(left<right) {
        if(!isalnum((unsigned char)s[left])) left++;
        else if(!isalnum((unsigned char)s[right])) right--;
        else if(tolower((unsigned char)s[left])!=tolower((unsigned char)s[right])) return false;
        else {left++;right--;}
    }
    return true;
}
