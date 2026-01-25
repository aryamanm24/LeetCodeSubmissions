class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        nums.sort()

        # [1, 4, 7, 9]

        length = len(nums)

        if(length == 1):
            return 0
        
        min_val = float('inf')

        for i in range(0, length-k+1):

            first_number = nums[i]
            second_number = nums[i+k-1]

            if(second_number - first_number < min_val):
                min_val = second_number - first_number
        
        return min_val