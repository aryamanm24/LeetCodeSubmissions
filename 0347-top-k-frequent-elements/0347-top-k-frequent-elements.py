from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        length = len(nums)
        
        count_map = defaultdict(int)

        for number in nums:
            count_map[number] += 1
        
        # {1: 4, 2: 4, 3: 2}

        buckets = [[] for _ in range(length+1)]

        # [[], [], [], [], [], [], [], [], [], [], []] -> since there are 10 elements in nums
        # and then max frequency that a number can take is the length of nums

        for num, freq in count_map.items():
            buckets[freq].append(num)
        
        # [[], [], [3], [], [1, 2], [], [], [], [], [], []]

        result = []

        for i in range(length, -1, -1):
            for num in buckets[i]:
                result.append(num)
                
                if(len(result) == k):
                    return result
        
        return []