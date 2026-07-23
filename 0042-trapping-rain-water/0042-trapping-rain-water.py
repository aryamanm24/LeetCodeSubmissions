class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        water_trapped = 0

        while(left <= right):

            if(left_max <= right_max):
                if(height[left] < left_max):
                    water_trapped += left_max - height[left]
                else:
                    left_max = max(left_max, height[left])
                left += 1
            
            else:
                if(height[right] < right_max):
                    water_trapped += right_max - height[right]
                else:
                    right_max = max(right_max, height[right])
                right -= 1
        
        return water_trapped