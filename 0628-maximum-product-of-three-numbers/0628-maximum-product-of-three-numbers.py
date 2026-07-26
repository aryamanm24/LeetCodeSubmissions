class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        nums.sort()

        last_three_product = nums[-1]*nums[-2]*nums[-3]
        first_two_neg_and_last_pos = nums[0]*nums[1]*nums[-1]

        return max(last_three_product, first_two_neg_and_last_pos)