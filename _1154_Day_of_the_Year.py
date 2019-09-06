import datetime


class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        # Approach 2
        Y, M, D = map(int, date.split('-'))
        return int((datetime.datetime(Y, M, D) - datetime.datetime(Y, 1, 1)).days + 1)

        # Approach 1
        # long_months = [1, 3, 5, 7, 8, 10, 12]
        # date = date.split('-')
        # year, month, day = int(date[0]), int(date[1]), int(date[2])
        # cur = 0
        # if month > 2:
        #     cur = 59
        #     if self.isLeapYear(year):
        #         cur = 60
        #     for m in xrange(3, month):
        #         if m in long_months:
        #             cur += 31
        #         else:
        #             cur += 30
        #
        # else:
        #     if month == 2:
        #         cur = 31
        # cur += day
        # return cur

    # def isLeapYear(self, year):
    #     if year % 100 == 0 and year % 400 != 0: return False
    #     return not year % 4
