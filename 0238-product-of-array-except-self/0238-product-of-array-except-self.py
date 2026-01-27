class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # [24, 12, 4, 1]
        # [1, 1, 2, 6]

        length = len(nums)
        prefix_product = [0]*length
        postfix_product = [0]*length

        prefix_product[0] = 1
        postfix_product[length-1] = 1

        for i in range(1, length):
            prefix_product[i] = prefix_product[i-1] * nums[i-1]
            postfix_product[length-1-i] = postfix_product[length-i] * nums[length-i]
        
        output = [0]*length

        for i in range(length):
            output[i] = prefix_product[i]*postfix_product[i]
        
        return output

        