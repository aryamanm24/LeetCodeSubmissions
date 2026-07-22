class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length_arr = len(nums) # O(n)

        left = [0]*(length_arr + 1)
        right = [0]*(length_arr + 1)
        left[0] = 1
        right[-1] = 1

        # Doing running direction in forward (left) and backward (right) direction
        # in one pass

        for i in range(1, length_arr+1):

            left[i] = nums[i-1]*left[i-1]
            right[length_arr - i] = nums[length_arr - i]*right[length_arr - i + 1]
        
        # Debugging printing
        # left_length = len(left)

        # for i in range(left_length):
        #     print(left[i], end=", ")
        
        # print()

        # for i in range(left_length):
        #     print(right[i], end=", ")

        output = [0]*length_arr

        for i in range(length_arr):
            output[i] = left[i] * right[i+1]
        
        return output