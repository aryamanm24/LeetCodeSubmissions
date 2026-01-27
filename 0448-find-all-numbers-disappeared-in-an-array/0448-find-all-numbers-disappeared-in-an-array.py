class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        frequency_map = {}

        for num in nums:
            if(num not in frequency_map):
                frequency_map[num] = True
        
        length = len(nums)
        missing = []

        for i in range(1, length+1):
            if(i not in frequency_map):
                missing.append(i)
        
        return missing