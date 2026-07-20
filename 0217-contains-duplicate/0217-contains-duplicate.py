class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # O(1) space solution:

        nums.sort()
        length = len(nums)

        for index in range(1, length):
            if(nums[index-1] == nums[index]):
                return True
        
        return False