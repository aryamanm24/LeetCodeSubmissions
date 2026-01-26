class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_map = {}

        for num in nums:
            if(num not in count_map):
                count_map[num] = 1
            count_map[num] += 1
        
        arr = []

        for key in count_map.keys():
            arr.append([count_map[key], key])
        
        sorted_arr = sorted(arr, reverse=True)

        output = []

        for i in range(k):
            output.append(sorted_arr[i][1])
        
        return output
