class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # To reduce the number the duplicate items:

        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1 & set2)