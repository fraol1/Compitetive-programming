class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        res = 0
        while left < right:
            if res < min(height[left],height[right])*(right-left):
                res = min(height[left],height[right])*(right-left)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return res