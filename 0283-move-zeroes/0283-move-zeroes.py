class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # A two pointer approach is very valid
        # But seeing the outputs for this problem, it seems that they're trying to maintain
        # the relative order

        #left = 0
        #right = len(nums)-1

        #while(left <= right):
            #if(nums[left] == 0 and nums[right] != 0):
                #nums[left], nums[right] = nums[right], nums[left]
                #left += 1
                #right -= 1
            
            #elif(nums[left] != 0 and nums[right] != 0):
                #left += 1
            
            #else:
                #left += 1
                #right -= 1
        
        # Maintaining relative order solution

        zero_index = 0
        non_zero_index = 0
        length = len(nums)

        while(zero_index <= length -1 and non_zero_index <=length-1):

            # How we want the swap to happen
            if(nums[zero_index] == 0 and nums[non_zero_index] != 0):
                nums[zero_index], nums[non_zero_index] = nums[non_zero_index], nums[zero_index]
                zero_index += 1
            
            # say both index values are zero, then just advance the non-zero index
            elif(nums[zero_index] == 0 and nums[non_zero_index] == 0):
                non_zero_index += 1
            
            elif(nums[zero_index] != 0 and nums[non_zero_index] == 0):
                # basically nothing as the non_zero_index is further down the array than
                # the zero_index
                zero_index += 1

            else:
                non_zero_index += 1