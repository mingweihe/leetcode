from datetime import datetime


class Solution(object):
    def dayOfTheWeek(self, d, m, y):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        wk = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        dt = datetime(int(y), int(m), int(d))
        return wk[dt.weekday()]
