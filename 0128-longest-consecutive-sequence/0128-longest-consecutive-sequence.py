class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        if(not nums):
            return 0
        
        num_set = set(nums)

        longest = 1

        for num in num_set:
            # if a previous element is not present in set - O(1) at avg.
            if(num-1 not in num_set):
                curr_length = 1
                curr_num = num + 1
                while(curr_num in num_set):
                    curr_length += 1
                    curr_num += 1
                
                longest = max(curr_length, longest)
        
        return longest