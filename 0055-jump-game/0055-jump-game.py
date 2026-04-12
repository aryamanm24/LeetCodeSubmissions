class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        final_position = len(nums)-1
        landing_position = len(nums)-2

        for i in range(landing_position, -1, -1):
            if(nums[i] + i >= final_position):
                final_position = i
        
        return final_position == 0