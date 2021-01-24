class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        def valid(a, b):
            if a == '??': return True
            if a[0] == '?': return a[1] == b[1]
            if a[1] == '?': return a[0] == b[0]
            return a == b
            
        hh = time[:2]
        mm = time[3:]
        for h in xrange(23, -1, -1):
            h = str(h).rjust(2, '0')
            if valid(hh, h):
                hh = h
                break
        for m in xrange(59, -1, -1):
            m = str(m).rjust(2, '0')
            if valid(mm, m):
                mm = m
                break
        return hh + ':' + mm
