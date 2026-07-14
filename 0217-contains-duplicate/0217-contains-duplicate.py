class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        number_map = {}

        for num in nums:
            if(num not in number_map):
                number_map[num] = 1
            else:
                return True
        
        return False