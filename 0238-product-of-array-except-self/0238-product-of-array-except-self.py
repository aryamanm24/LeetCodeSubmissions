class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)

        left = [0]*(length+1)
        right = [0]*(length+1)

        left[0] = 1
        right[-1] = 1

        # left = [1, 0, 0, 0]
        # right = [0, 0, 0, 1]
        # nums = [1, 2, 3, 4]
        for i in range(1, length+1):

            left[i] = left[i-1] * nums[i-1]
            
            # right[3]
            right[length-i] = right[length-i+1] * nums[length-i]
        
        # print(left)
        # print(right)

        product = [0] *length

        for i in range(length):
            product[i] = left[i]*right[i+1]
        
        return product

