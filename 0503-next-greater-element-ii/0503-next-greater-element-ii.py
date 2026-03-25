class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        # Duplicating the array twice
        length = len(nums)
        new_arr = [0]*(2*length)
        # [1, 2, 1] => [1, 2, 1, 1, 2, 1] # i + length
        for i, num in enumerate(nums):
            new_arr[i], new_arr[i+ length] = num, num
        
        # Created the double-length array, and now just perform monotonic stack
        stack = [] # Store values
        result = [-1]*length

        for i, num in enumerate(new_arr):

            while(stack and nums[stack[-1]] < num):
                result[stack[-1]] = num # Taking the circular arr in consideration
                stack.pop()
            
            if(i < length):
                stack.append(i)
        
        return result