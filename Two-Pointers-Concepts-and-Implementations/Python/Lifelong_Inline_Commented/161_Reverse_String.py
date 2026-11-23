# Reverse String
# Reverse the characters in place. Swap the two outside characters, then move inside.
# Time O(n). Extra space O(1). Python input is a mutable list.

def solve(chars):
    left = 0
    right = len(chars) - 1
    while left < right:
        # Save the left character before overwriting it.
        saved = chars[left]
        chars[left] = chars[right]
        chars[right] = saved
        # Both outside characters are now in their final places.
        left += 1
        right -= 1
    return chars
