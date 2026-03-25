class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        # Sort the array first
        nums.sort() # nlogn
        result = [] # list of all triplets
        length = len(nums)

        for i in range(length-2):

            if(i > 0 and nums[i] == nums[i-1]):
                continue

            
            left, right = i+1, len(nums) - 1

            while(left < right):

                sum_val = nums[left] + nums[right] + nums[i]
                if(sum_val == 0):
                    append_list = [nums[left], nums[right], nums[i]]
                    result.append(append_list)
                    while(left < right and nums[left] == nums[left+1]):
                        left += 1
                    while(left < right and nums[right] == nums[right-1]):
                        right -= 1
                

                    left += 1
                    right -= 1
                
                elif(sum_val < 0):
                    left += 1
                else:
                    right -= 1
        
        return result

