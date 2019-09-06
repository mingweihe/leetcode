class Solution(object):
    def compareVersion(self, v1, v2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # Approach 2
        v1, v2 = v1.split('.'), v2.split('.')
        for i in xrange(max(len(v1), len(v2))):
            num1 = int(v1[i]) if i < len(v1) else 0
            num2 = int(v2[i]) if i < len(v2) else 0
            if num1 < num2: return -1
            elif num1 > num2: return 1
        return 0
        # Approach 1
        # def pre_processing(x):
        #     x = map(int, x.split('.'))
        #     while len(x) > 1 and x[-1] == 0: x.pop()
        #     return x
        # v1 = pre_processing(v1)
        # v2 = pre_processing(v2)
        # if v1 > v2: return 1
        # if v1 < v2: return -1
        # return 0
