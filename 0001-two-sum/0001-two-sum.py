class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        number_map = {}

        for index, num in enumerate(nums):
            if(target-num not in number_map):
                number_map[num] = index
            else:
                return [index, number_map[target-num]]