from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        number_count = Counter(nums)

        # {1: 4, 2: 4, 3: 2}
        result = []

        most_common = number_count.most_common()
        for i in range(k):
            result.append(most_common[i][0])
        
        return result
