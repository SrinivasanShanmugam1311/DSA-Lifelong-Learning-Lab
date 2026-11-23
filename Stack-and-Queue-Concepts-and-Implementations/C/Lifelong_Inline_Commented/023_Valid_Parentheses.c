// STEP-BY-STEP LOGIC
// Use a stack to remember opening brackets that have not been closed.
// Push each opening bracket onto the stack.
// For a closing bracket, the most recent opening bracket must be its matching type.
// If the stack is empty or the types differ, return false.
// Remove the matched opening bracket.
// At the end the stack must be empty. Input is restricted to the six bracket characters.
// Original implementation follows.

// Valid Parentheses
// Push opening brackets. Each closing bracket must match the last opening bracket. The stack must end empty.
// O(n) time, O(n) space
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
bool solve(const char *s) {
    char *stack=malloc(strlen(s)+1); int top=0;
    for(int i=0;s[i];i++) {
        char ch=s[i];
        if(ch=='(' || ch=='[' || ch=='{') stack[top++]=ch;
        else {
            char want=ch==')'?'(':ch==']'?'[':'{';
            if(top==0 || stack[--top]!=want) {free(stack);return false;}
        }
    }
    bool ok=top==0;free(stack);return ok;
}
