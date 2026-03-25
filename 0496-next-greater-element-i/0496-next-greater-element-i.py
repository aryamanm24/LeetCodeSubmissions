class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hash_map = {}

        for i, num in enumerate(nums1):
            hash_map[num] = i
        
        stack = [] # Store numbers in this?
        result = [-1]*len(nums1)

        for i, num in enumerate(nums2):

            while(stack and num > stack[-1]):
                if(stack[-1] in hash_map):
                    result[hash_map[stack[-1]]] = num
                stack.pop()
                
            stack.append(num)
        
        return result
