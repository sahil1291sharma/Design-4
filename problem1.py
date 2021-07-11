class Twitter:
    
    class Tweet:
        def __init__(self, createdAt, tID):
            self.tID = tID
            self.createdAt = createdAt

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.userMap = {}
        self.tweetList = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.follow(userId, userId)
        if userId not in self.tweetList:
            self.tweetList[userId] = []
        self.tweetList[userId].append(self.Tweet(self.time, tweetId))
        self.time +=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        pq = []
        result = []
        if self.userMap:
            fIds = self.userMap[userId]
            if fIds:
                for fId in fIds:
                    if fId in self.tweetList:
                        twtList = self.tweetList[fId]
                        if twtList:
                            for twt in twtList:
                                heapq.heappush(pq,(twt.createdAt,twt.tID)) #heapq does not support class compare, can use tuples instead of Tweet class -> need to check that
                                if len(pq) > 10:
                                    heapq.heappop(pq)

        for _ in range(len(pq)):
            result.insert(0,heapq.heappop(pq)[1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.userMap:
            self.userMap[followerId] = set()
        self.userMap[followerId].add(followeeId)
        #print(self.userMap)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.userMap and followeeId != followerId:
            if followeeId in self.userMap[followerId]:
                self.userMap[followerId].remove(followeeId)
        #print(self.userMap)
            
#Time complexity O(nlogk) for inserting into the priority queue and O(1) for getting the feed as there are 10 tweets to get
#space complexity is O(n) for tweets table and O(k*k) for users table where k is number of users and worst case each user follows every other user