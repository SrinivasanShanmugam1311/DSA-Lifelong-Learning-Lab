# STEP-BY-STEP LOGIC
# Use a stack to remember opening brackets that have not been closed.
# Push each opening bracket onto the stack.
# For a closing bracket, the most recent opening bracket must be its matching type.
# If the stack is empty or the types differ, return false.
# Remove the matched opening bracket.
# At the end the stack must be empty. Input is restricted to the six bracket characters.
# Original implementation follows.

# Valid Parentheses
# Push opening brackets. Each closing bracket must match the last opening bracket. The stack must end empty.
# O(n) time, O(n) space
def solve(s):
    stack=[]
    pairs={')':'(',']':'[','}':'{'}
    for ch in s:
        if ch in '([{': stack.append(ch)
        elif not stack or stack.pop()!=pairs[ch]: return False
    return not stack
