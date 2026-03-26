class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums)-1

        while(left < right):
            mid = (left+right)//2

            # the case where the min lies to the right of mid
            # due to rotation
            if(nums[mid] > nums[right]):
                left = mid+1
            else:
                right = mid
        
        return nums[left]
        
