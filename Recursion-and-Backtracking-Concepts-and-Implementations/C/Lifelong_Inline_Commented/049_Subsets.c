// STEP-BY-STEP LOGIC
// Start with an empty path. It is already a valid subset.
// Save a copy of the path at every recursive call.
// Try each available element starting at start.
// Choose the element by placing it at the end of the path.
// Explore with i + 1 so the same position is not selected twice.
// Undo the choice before trying a sibling. Python pops; C restores the logical length by returning from recursion.
// The result contains every subset once for distinct input values.
// Original implementation follows.

// Subsets
// Save the current path. Choose each remaining element, explore, then undo the choice.
// O(n*2^n) time including output, O(n) auxiliary space
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
/* Emit each subset through a callback; callback must copy if retaining it. */
void dfs(int *a,int n,int start,int *path,int depth,void (*emit)(int *,int)) {
    emit(path,depth);
    for(int i=start;i<n;i++) {
        path[depth]=a[i];
        dfs(a,n,i+1,path,depth+1,emit);
    }
}
void solve(int *a,int n,void (*emit)(int *,int)) {
    int *path=malloc((n+1)*sizeof(int));
    dfs(a,n,0,path,0,emit);free(path);
}
