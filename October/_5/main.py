class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))


print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))
