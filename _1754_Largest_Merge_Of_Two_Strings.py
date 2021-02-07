class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ## Approach 2, conciser
        res = ''
        while word1 and word2:
            if word1 < word2:
                res += word2[0]
                word2 = word2[1:]
            else:
                res += word1[0]
                word1 = word1[1:]
        res += word1 + word2
        return res
    
        ## Approach 1
#         def pick_first(i, j):
#             while i < m and j < n:
#                 if word1[i] == word2[j]:
#                     i += 1
#                     j += 1
#                 else:
#                     if word1[i] > word2[j]: return True
#                     else: return False
#             if i == m: return False
#             if j == n: return True
                    
#         m, n = len(word1), len(word2)
#         i, j = 0, 0
#         res = []
#         while i < m and j < n:
#             if pick_first(i, j):
#                 res += word1[i]
#                 i += 1
#             else:
#                 res += word2[j]
#                 j += 1
#         if i == m: res += word2[j:]
#         else: res += word1[i:]
#         return ''.join(res)
