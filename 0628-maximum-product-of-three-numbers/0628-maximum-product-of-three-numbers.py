class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        max_1, max_2, max_3 = float('-inf'), float('-inf'), float('-inf')
        min_1, min_2 = float('inf'), float('inf')

        for num in nums:
            if(num >= max_1):
                max_3 = max_2
                max_2 = max_1
                max_1 = num
            elif(max_2 <= num):
                max_3 = max_2
                max_2 = num
            elif(max_3 <= num):
                max_3 = num

            
            if(num < min_1):
                min_2 = min_1
                min_1 = num
            elif(num <= min_2):
                min_2 = num
        
        return max(max_1*max_2*max_3, max_1*min_1*min_2)