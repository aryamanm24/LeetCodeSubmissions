class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hash_map = {}

        for num in nums:

            if(num in hash_map.keys()):
                return True
            
            hash_map[num] = 1
        
        return False