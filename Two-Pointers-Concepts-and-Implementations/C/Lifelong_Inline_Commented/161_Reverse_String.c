/*
Reverse String
Reverse the characters in place. Swap the two outside characters, then move inside.
Time O(n). Extra space O(1). Python input is a mutable list.
*/

void solve(char *chars, int n)
{
    int left = 0;
    int right = n - 1;
    while (left < right) {
        /* Save the left character before overwriting it. */
        char saved = chars[left];
        chars[left] = chars[right];
        chars[right] = saved;
        /* Both outside characters are now in their final places. */
        left++;
        right--;
    }
}
