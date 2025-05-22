class Solution(object):
    def intersection(self, nums1, nums2):
        
        # set vai tirar todas as duplicatas e deixar apenas uma cópia e o & vai unir apenas as interceções
        return list(set(nums1) & set(nums2))
