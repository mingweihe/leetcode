import collections
import itertools
import heapq


class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
            libs & funcs:
            deque, itertools.count, set
            heapq.merge, itertoos.islice
        """
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)
        self.timer = itertools.count(step=-1)

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweets[userId].appendleft([next(self.timer), tweetId])

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        users = self.followees[userId]
        users_tweets = [self.tweets[uid] for uid in users | {userId}]
        tweets = itertools.islice(heapq.merge(*users_tweets), 10)
        return [t for _, t in tweets]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followees[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
