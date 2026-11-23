# Container With Most Water
# O(n) time; O(1) extra space. Example [1,8,6,2,5,4,8,3,7] gives 49. Heights follow standard LeetCode constraints.
def solve(height):
    # Start with the widest possible container.
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        # The shorter wall limits the water, because water overflows it.
        left_height = height[left]
        right_height = height[right]
        width = right - left
        if left_height <= right_height:
            water_height = left_height
        else:
            water_height = right_height
        current_area = width * water_height
        # Remember the best answer before discarding a wall.
        if current_area > max_area:
            max_area = current_area
        # Keeping the shorter wall cannot improve the area.
        # The width would shrink and the water height cannot rise.
        # Move the shorter wall to look for a taller one.
        if left_height <= right_height:
            left += 1
        else:
            right -= 1
    return max_area
