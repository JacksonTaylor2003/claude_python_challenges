def max_area(heights):
    left = 0
    right = len(heights) - 1
    area_max = (right - left) * min(heights[left], heights[right])

    while left < right:
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

        area_current = (right - left) * min(heights[left], heights[right])
        if area_current > area_max:
            area_max = area_current
            
    return area_max

max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
# 49
# The best choice is index 1 (height 8) and index 8 (height 7):
# width = 8-1 = 7, height = min(8,7) = 7, area = 7*7 = 49
max_area([1, 1])
# 1   (only one possible pair: width=1, height=min(1,1)=1)