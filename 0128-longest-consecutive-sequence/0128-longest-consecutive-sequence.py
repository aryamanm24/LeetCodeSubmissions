class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if(not nums):
            return 0
        
        number_set = set(nums)

        longest_seq = 1

        for num in number_set:
            
            if(num-1 not in number_set):
                curr_length = 1

                while(num+1 in number_set):
                    num += 1
                    curr_length += 1
                
                longest_seq = max(longest_seq, curr_length)

            else:
                num += 1
        
        return longest_seq