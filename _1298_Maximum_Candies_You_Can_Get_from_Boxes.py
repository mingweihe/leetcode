class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        # Approach 2
        cur_keys = set(i for i in xrange(len(status)) if status[i])
        cur_boxes = set(initialBoxes)
        res = set()
        open_boxes = True
        while open_boxes:
            open_boxes = cur_keys & cur_boxes
            res |= open_boxes
            cur_boxes -= open_boxes
            for idx in open_boxes:
                cur_keys |= set(keys[idx])
                cur_boxes |= set(containedBoxes[idx])
        return sum(candies[i] for i in res)

        # Approach 1
        # res = 0
        # found_keys, closed_boxes, open_boxes = set(), set(), set()
        # for idx in initialBoxes:
        #     if status[idx]: open_boxes.add(idx)
        #     else: closed_boxes.add(idx)
        # while open_boxes:
        #     idx = open_boxes.pop()
        #     res += candies[idx]
        #     for key_id in keys[idx]:
        #         found_keys.add(key_id)
        #         if key_id in closed_boxes:
        #             open_boxes.add(key_id)
        #             closed_boxes.discard(key_id)
        #     for box_id in containedBoxes[idx]:
        #         if status[box_id] == 1:
        #             open_boxes.add(box_id)
        #         elif status[box_id] == 0 and box_id in found_keys:
        #             open_boxes.add(box_id)
        #             closed_boxes.discard(box_id)
        #         else: closed_boxes.add(box_id)
        # return res
