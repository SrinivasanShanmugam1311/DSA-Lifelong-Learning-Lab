# STEP-BY-STEP LOGIC
# Start with an empty path. It is already a valid subset.
# Save a copy of the path at every recursive call.
# Try each available element starting at start.
# Choose the element by placing it at the end of the path.
# Explore with i + 1 so the same position is not selected twice.
# Undo the choice before trying a sibling. Python pops; C restores the logical length by returning from recursion.
# The result contains every subset once for distinct input values.
# Original implementation follows.

# Subsets
# Save the current path. Choose each remaining element, explore, then undo the choice.
# O(n*2^n) time including output, O(n) auxiliary space
def solve(a):
    result=[]
    path=[]
    def dfs(start):
        result.append(path.copy())
        for i in range(start,len(a)):
            path.append(a[i])
            dfs(i+1)
            path.pop()
    dfs(0)
    return result
