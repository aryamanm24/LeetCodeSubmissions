from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefixsum_freq = defaultdict(int)

        # the prefix sum of 0 appears once
        prefixsum_freq[0] = 1

        counts = 0
        running_sum = 0

        for num in nums:

            running_sum += num
            complement_prefixsum = running_sum - k
            if(complement_prefixsum in prefixsum_freq):
                counts += prefixsum_freq[complement_prefixsum]
            
            prefixsum_freq[running_sum] += 1
        
        return counts

