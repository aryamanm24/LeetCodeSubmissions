class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        length = len(nums)

        # Optimal solution using DP
        longest_subsequence = [1]*length

        # [10, 9, 2, 5, 3, 7, 101, 18]

        for i in range(1, length):
            for j in range(0, i):

                if(nums[j] < nums[i]):
                    longest_subsequence[i] = max(longest_subsequence[i], longest_subsequence[j]+1)

        # Now, just find the max in longest_subsequence
        max_len = float('-inf')
        for i in range(length):
            if(longest_subsequence[i] > max_len):
                max_len = longest_subsequence[i]
        
        return max_len