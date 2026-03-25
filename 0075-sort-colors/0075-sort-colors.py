class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Dutch-algorithm
        left = 0
        right = len(nums)-1
        mid = 0

        while(mid <= right):
            if(nums[mid] == 2): # definitely swap with right
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
            
            elif(nums[mid] == 0): # swap with left as mid should have 1s
                nums[left], nums[mid] = nums[mid], nums[left]
                mid+=1
                left +=1
            
            else:
                mid += 1

