class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if(len(nums) == 1):
            return 1
        
        slow = 0
        fast = 1
        length = len(nums)
        while(fast < length):
            if(nums[fast] != nums[slow]):
                # swap nums[slow+1] with nums[fast], inc. counter, inc. fast
                # inc. slow
                slow += 1
                nums[slow], nums[fast] = nums[fast], nums[slow]
            fast += 1
        
        return slow + 1