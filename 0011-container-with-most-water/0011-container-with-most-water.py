class Solution:
    def maxArea(self, height: List[int]) -> int:
       beg = 0
       end = len(height) - 1 
       max_area = 0

       while beg < end:
            area = min(height[beg], height[end]) * (end - beg)
            max_area = max(area, max_area)

            if height[beg] < height[end]:
                beg += 1
            else:
                end -= 1
       return  max_area