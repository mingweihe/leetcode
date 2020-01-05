import collections


class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        visited = {id}
        visited |= set(friends[id])
        cur_level = 1
        cur_people = friends[id]
        while cur_level < level:
            temp = []
            for people_id in cur_people:
                for to_add in friends[people_id]:
                    if to_add not in visited:
                        temp += to_add,
                        visited.add(to_add)
            cur_people = temp
            cur_level += 1
        dic = collections.defaultdict(int)
        for people_id in cur_people:
            for v_id in watchedVideos[people_id]:
                dic[v_id] += 1
        res = sorted(dic.items(), key=lambda x: (x[1], x[0]))
        return [x[0] for x in res]
