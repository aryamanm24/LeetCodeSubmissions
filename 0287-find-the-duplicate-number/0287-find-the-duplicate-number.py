class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # Phase 1: to find the intersection (of the loop in the array)
        fast = nums[0]
        slow = nums[0]

        while(True):
            slow = nums[slow]
            fast = nums[nums[fast]]

            if(slow == fast):
                break
        
        # Phase 2: finding the starting point of the loop
        # because the intersection of the loop may not be the start
        slow = nums[0]

        while(slow != fast):
            slow = nums[slow]
            fast = nums[fast]

        return slow