class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        if(not nums):
            return 0

        counts = {}
        counts[0] = 1

        prefix_sum = 0
        result = 0

        for i, num in enumerate(nums):

            prefix_sum += num
            target = prefix_sum - k

            if(target in counts):
                result += counts[target]
            if(prefix_sum in counts):
                counts[prefix_sum] += 1
            else:
                counts[prefix_sum] = 1
        
        return result