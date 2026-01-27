class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count_map = {}

        for num in nums:
            if(num not in count_map):
                count_map[num] = 1
            else:
                count_map[num] += 1

        length = len(nums)

        for key in count_map.keys():
            if(count_map[key]/length > 0.50):
                return key
        
        return -1