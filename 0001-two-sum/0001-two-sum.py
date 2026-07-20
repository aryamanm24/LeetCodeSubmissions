class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        number_index_map = {}

        for index, num in enumerate(nums):

            complement = target - num
            if(complement in number_index_map):
                return [index, number_index_map[complement]]
            else:
                number_index_map[num] = index
        
        return [-1, -1]