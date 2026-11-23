# STEP-BY-STEP LOGIC
# left marks the start of a window without duplicates.
# right reads one new character at a time.
# Remember the most recent index of each character. An unseen character has index -1.
# If the previous occurrence is inside the window, move left just past it. Never move left backward.
# Record the new last index and compute right - left + 1.
# Keep the largest valid length.
# Original implementation follows.

# Longest Substring Without Repeating Characters
# Remember the last index of each character. If it is inside the window, move left past it. Update the longest length. ASCII input.
# O(n) time, O(1) space for fixed alphabet
def solve(s):
    last={}
    left=best=0
    for right,ch in enumerate(s):
        left=max(left,last.get(ch,-1)+1)
        last[ch]=right
        best=max(best,right-left+1)
    return best
