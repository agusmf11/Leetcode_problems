class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1 = sorted(nums1 + nums2)
        if (len(nums1))%2 == 0:
            n = (nums1[int(len(nums1)/2)-1] + nums1[(int(len(nums1)/2))])/2
            return n
        else:
            n = nums1[int(len(nums1)/2)] 
            return n
        
nums1 = []
nums2 = [2,3]

solver = Solution()

print(solver.findMedianSortedArrays(nums1, nums2))