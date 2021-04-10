from collections import deque


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        st = set()
        qu = deque([0])
        while qu:
            key = qu.popleft()
            st.add(key)
            for nk in rooms[key]:
                if nk in st: continue
                qu.append(nk)
        return len(st) == len(rooms)
