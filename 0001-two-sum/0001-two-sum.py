class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}

        for i, num in enumerate(nums):

            if(target-num not in hash_map):
                hash_map[num] = i

            else:
                return [i, hash_map[target-num]]