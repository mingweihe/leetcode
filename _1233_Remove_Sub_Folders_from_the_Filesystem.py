class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort()
        cur = folder[0]
        res = []
        for i in xrange(1, len(folder)):
            if folder[i].startswith(cur + '/'):
                continue
            res.append(cur)
            cur = folder[i]
        res.append(cur)
        return res
