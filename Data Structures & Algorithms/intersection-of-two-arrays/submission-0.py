from collections import Counter 
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique1 = set(nums1)
        unique2 = set(nums2)
        both = []
        for i in unique1:
            if i in unique2:
                both.append(i)
        return both

