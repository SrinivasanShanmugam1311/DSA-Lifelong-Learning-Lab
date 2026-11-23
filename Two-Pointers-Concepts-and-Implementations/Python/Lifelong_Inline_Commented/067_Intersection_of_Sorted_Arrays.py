# Intersection of Sorted Arrays
# O(n+m) time; O(1) auxiliary space excluding output. Assumption: unique sorted intersection. [1,2,2,4] and [2,2,3,4] give [2,4].
def solve(first, second):
    # Both arrays are sorted. Read each from its beginning.
    left = 0
    right = 0
    result = []
    while left < len(first) and right < len(second):
        # A smaller value cannot match any later value in the other array.
        if first[left] < second[right]:
            left += 1
        elif first[left] > second[right]:
            right += 1
        else:
            # Both values match. Keep each common value only once.
            value = first[left]
            if not result or result[-1] != value:
                result.append(value)
            left += 1
            right += 1
    return result
