class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Approach 2
        # set operations: | ^ &
        return list(set(nums1) & set(nums2))

        # Approach 1
        # d, res = {}, []
        # for i in nums1: d[i] = 0
        # for i in nums2:
        #     if i in d and d[i] == 0:
        #         res.append(i)
        #         d[i] = 1
        # return res
