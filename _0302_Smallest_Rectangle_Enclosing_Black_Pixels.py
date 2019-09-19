class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        # Approach 2 binary search time O(m*log(n)+n*log(m))
        # BTW, x, y is necessary for binary search
        # otherwise, we can't decide which part to select
        if not image: return 0

        def search(i, j, check):
            # discriminate  i < j and i <= j
            while i < j:
                mid = (i + j) / 2
                if check(mid): j = mid
                else: i = mid + 1
            return i

        top = search(0, x, lambda idx: '1' in image[idx])
        bottom = search(x + 1, len(image), lambda idx: '1' not in image[idx])
        left = search(0, y, lambda idx:  any([image[i][idx] == '1' for i in xrange(len(image))]))
        right = search(y + 1, len(image[0]), lambda idx: all([image[i][idx] == '0' for i in xrange(len(image))]))
        return (bottom - top) * (right - left)

        # Approach 1 naive dfs time O(m*n),
        # this is general for any number of black regions
        # if not image: return 0
        # directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        # def dfs(i, j, b, visited):
        #     for i1, j1 in directions:
        #         i2, j2 = i+i1, j+j1
        #         if i2 < 0 or i2 == len(image) or j2 < 0 or j2 == len(image[0]):
        #             continue
        #         if (i2, j2) in visited: continue
        #         if image[i2][j2] == '0': continue
        #         visited.add((i2, j2))
        #         b[0] = min(b[0], i2)
        #         b[1] = max(b[1], i2)
        #         b[2] = min(b[2], j2)
        #         b[3] = max(b[3], j2)
        #         dfs(i2, j2, b, visited)
        # boundary = [x, x, y, y]
        # dfs(x, y, boundary, set())
        # x1, x2, y1, y2 = boundary
        # return (x2-x1+1)*(y2-y1+1)
