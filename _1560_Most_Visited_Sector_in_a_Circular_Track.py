class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        ## Approach 2
        return range(rounds[0], rounds[-1]+1) or range(1, rounds[-1]+1) + range(rounds[0], n+1)

        ## Approach 1
#         rounds = [rounds[0]-1] + rounds
#         cnt = defaultdict(int)
#         for i in xrange(1, len(rounds)):
#             start = rounds[i-1]
#             end = rounds[i]
#             if start <= end:
#                 for j in xrange(start+1, end+1):
#                     cnt[j] += 1
                    
#             else:
#                 for j in xrange(start+1, n+1):
#                     cnt[j] += 1
#                 for j in xrange(1, end+1):
#                     cnt[j] += 1
#         maxi = max(cnt.values())
#         res = [k for k, v in cnt.items() if v == maxi]
#         return sorted(res)
