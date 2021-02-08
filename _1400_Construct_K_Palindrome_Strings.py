from collections import Counter


class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        # Approach 2, conciser
        return sum(x & 1 for x in Counter(s).values()) <= k <= len(s)
    
        # Approach 1
        # if len(s) < k: return False
        # cnts = Counter(s).values()
        # num_odd = len(filter(lambda x: x & 1, cnts))
        # if num_odd > k: return False
        # num_needed = k - num_odd
        # num_even = (len(s) - num_odd)
        # if num_needed & 1:
        #     num_even -= 2
        #     num_needed -= 1
        # return num_even >= num_needed
