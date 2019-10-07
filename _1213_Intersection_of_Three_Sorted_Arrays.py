class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        # Approach 3 set time O(n*log(n))
        return sorted(set(arr1) & set(arr2) & set(arr3))

        # Approach 2 hashtable time O(n)
        #   no need to sort, because default order of dictionary is order of insertion
        # return [k for k, v in collections.Counter(arr1+arr2+arr3).items() if v == 3]

        # Approach 1 straightforward time O(n)
        # i, j, k = 0, 0, 0
        # a, b, c = len(arr1), len(arr2), len(arr3)
        # res = []
        # while i < a and j < b and k < c:
        #     if arr1[i] == arr2[j] == arr3[k]:
        #         res.append(arr1[i])
        #         i += 1
        #         j += 1
        #         k += 1
        #     elif arr1[i] < arr2[j]: i += 1
        #     elif arr2[j] < arr3[k]: j += 1
        #     else: k += 1
        # return res
