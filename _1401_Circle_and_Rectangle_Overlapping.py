class Solution(object):
    def checkOverlap(self, radius, x_center, y_center, x1, y1, x2, y2):
        """
        :type radius: int
        :type x_center: int
        :type y_center: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        # Approach 2, O(1), conciser
        x1, x2, y1, y2 = x1-x_center, x2-x_center, y1-y_center, y2-y_center
        min_x = 0 if x1 * x2 <= 0 else min(x1*x1, x2*x2)
        min_y = 0 if y1 * y2 <= 0 else min(y1*y1, y2*y2)
        return min_x + min_y <= radius * radius
        
        # Approach 2, O(1)
        # for x, y in [[x1, y1], [x1, y2], [x2, y1], [x2, y2]]:
        #     if (x - x_center) ** 2 + (y - y_center) ** 2 <= radius ** 2:
        #         return True
        # for x in [x1, x2]:
        #     if x_center - radius <= x <= x_center + radius and y1 <= y_center <= y2:
        #         return True
        # for y in [y1, y2]:
        #     if y_center - radius <= y <= y_center + radius and x1 <= x_center <= x2:
        #         return True
        # return x1 <= x_center <= x2 and y1 <= y_center <= y2
        
        # Approach 1, O(n^2) check all points in circle
        # for x in xrange(x_center-radius, x_center+radius+1):
        #     for y in xrange(y_center-radius, y_center+radius+1):
        #         if x < x1 or x > x2 or y < y1 or y > y2: continue
        #         if (x-x_center) ** 2 + (y-y_center) ** 2 <= radius ** 2 and x1 <= x <= x2 and y1 <= y <= y2:
        #             return True
        # return False
