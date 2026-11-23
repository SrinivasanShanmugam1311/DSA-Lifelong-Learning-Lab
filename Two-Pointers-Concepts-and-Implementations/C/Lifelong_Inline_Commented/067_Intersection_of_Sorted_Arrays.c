/* Intersection of Sorted Arrays
 * O(n+m) time; O(1) auxiliary space excluding output. Assumption: unique sorted intersection. [1,2,2,4] and [2,2,3,4] give [2,4].
 */
/* Caller supplies result with room for min(n,m) integers. */
int solve(const int first[], int n, const int second[], int m, int result[]) {
    int left = 0;
    int right = 0;
    int count = 0;
    while (left < n && right < m) {
        /* A smaller value cannot match a later value in the other array. */
        if (first[left] < second[right])
            left++;
        else if (first[left] > second[right])
            right++;
        else {
            /* Keep each common value only once. */
            int value = first[left];
            if (count == 0 || result[count - 1] != value)
                result[count++] = value;
            left++;
            right++;
        }
    }
    return count;
}
