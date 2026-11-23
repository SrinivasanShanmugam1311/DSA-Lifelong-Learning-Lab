# STEP-BY-STEP LOGIC
# Start with one pointer at each end.
# Skip punctuation on either side. It is not part of the comparison.
# Convert the two remaining characters to lowercase before comparing.
# If they differ, the string cannot be a palindrome.
# If they match, move both pointers inward. Those characters need no further checking.
# When the pointers meet or cross, every required pair has matched.
# Original implementation follows.

# Valid Palindrome
# Skip punctuation at both ends. Compare lowercase letters or digits. Move inward after a match.
# O(n) time, O(1) space (ASCII input)
def solve(s):
    left,right=0,len(s)-1
    while left<right:
        if not s[left].isalnum(): left+=1
        elif not s[right].isalnum(): right-=1
        elif s[left].lower()!=s[right].lower(): return False
        else: left+=1;right-=1
    return True
