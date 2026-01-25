class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        length = len(nums)

        circular = []
        circular += nums
        circular += nums

        output = [-1]*length
        stack = [] # will keep track of the indices

        for i in range(2*length):
            actual_i = i % length

            while(stack and nums[stack[-1]] < nums[actual_i]):
                output[stack[-1]] = nums[actual_i]
                stack.pop()
            
            if(actual_i < length):
                stack.append(actual_i)
        
        return output