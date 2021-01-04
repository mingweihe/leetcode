class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        d = {}
        ans = []
        for name in names:
            if name not in d:
                ans += name,
                d[name] = 0
            else:
                d[name] += 1
                cur_name = name + '(' + str(d[name]) + ')'
                while cur_name in d:
                    d[name] += 1
                    cur_name = name + '(' + str(d[name]) + ')'
                d[cur_name] = 0
                ans += cur_name,
        return ans
