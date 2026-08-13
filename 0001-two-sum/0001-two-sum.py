class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        number_index_map = {}

        for index, num in enumerate(nums):

            if(target-num not in number_index_map):
                number_index_map[num] = index
            
            else:
                return [index, number_index_map[target-num]]
        return [-1, -1]