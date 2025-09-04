# Social Media Platform - Intermediate OOP Challenge
# Build a simplified social media system:

# User Class

# Initialize with: username, email, bio
# Has posts list, followers list (User objects), following list (User objects), blocked_users list
# Has is_private boolean (default False)
# Has follow(other_user) method that adds to following and other_user's followers
# Has unfollow(other_user) method
# Has create_post(content, post_type="text") method that creates and adds Post to posts
# Has get_follower_count() and get_following_count() methods
# Has get_recent_posts(days=7) method returning posts from last N days
# Has can_view_profile(viewer_user) method (handles private profiles)
# Has get_mutual_followers(other_user) method returning list of users who follow both
# Has get_activity_level() method returning "low", "medium", "high" based on posting frequency
# Has block_user(user_to_block) method adding user to blocked list
# Has is_blocked(other_user) method checking if other_user is blocked
# Has get_post_count() method returning total number of posts made
# Has get_average_post_engagement() method returning average likes/comments across all posts

# Post Class

# Initialize with: author (User object), content, post_type ("text", "image", "video")
# Has timestamp (use current date/time), likes list (User objects), comments list
# Has is_edited boolean, view_count integer
# Has like(user) and unlike(user) methods
# Has add_comment(user, comment_text) method that creates Comment object
# Has get_like_count() method
# Has get_engagement_score() method combining likes, comments, and views
# Has is_trending() method based on recent engagement
# Has get_top_comments(limit=3) method returning most liked comments
# Has has_hashtags() method checking if post contains #hashtags
# Has extract_hashtags() method returning list of hashtags in the post content
# Has get_age_in_days() method returning days since post was created
# Has edit_content(new_content) method updating post content and setting is_edited to True

# Comment Class

# Initialize with: author (User object), content, parent_post (Post object)
# Has timestamp, likes list, replies list (other Comment objects)
# Has like(user) and unlike(user) methods
# Has add_reply(user, reply_text) method for nested comments
# Has get_like_count() method
# Has get_reply_count() method returning number of replies to this comment
# Has get_total_engagement() method returning likes on comment + likes on all replies
# Has is_by_post_author() method checking if comment author is same as post author

# SocialNetwork Class

# Initialize with: platform_name
# Has users dictionary (username as key), all_posts list
# Has register_user(username, email, bio) method
# Has find_user(username) method for login purposes
# Has search_users(username) method for partial search purposes
# Has get_trending_posts(limit=10) method returning most engaging recent posts
# Has get_user_feed(user, limit=20) method showing posts from people they follow
# Has search_posts(keyword) method returning posts containing the keyword
# Has get_suggested_users(user, limit=5) method suggesting people to follow
# Has get_platform_stats() method returning total users, posts, engagement metrics
# Has get_most_active_users(limit=10) method returning users with most posts/engagement
# Has get_hashtag_trends() method extracting #hashtags from all posts and returning frequency count
# Has moderate_content(post) method checking for inappropriate content using keyword filtering
# Has get_user_statistics(user) method returning comprehensive stats: posts, followers, engagement rates
# Has find_influencers(min_followers=1000) method returning users above follower threshold
# Has get_daily_active_users(date) method counting users who posted on a specific date

import datetime
from better_profanity import profanity

class User:
    def __init__(self, username, email, bio):
        self.username = username
        self.email = email
        self.bio = bio
        self.posts = []
        self.followers = []
        self.following = []
        self.blocked_users = []
        self.is_private = False
    
    def follow(self, other_user):
        self.following.append(other_user)
        other_user.followers.append(self)

        # user1.follow(user2)
        # print(user1.following[0].username)
        # print(user2.followers[0].username)
        # print(user1.following)
        # print(user2.followers)
    
    def unfollow(self, other_user):
        self.following.remove(other_user)
        other_user.followers.remove(self)

        # user1.unfollow(user2)
        # print(user1.following)
        # print(user2.followers)

    def create_post(self, content, post_type="text"):
        self.posts.append(Post(self, content, post_type))

        # user1.create_post("This is my first post!", "image")
        # user1.create_post("This is my second post!")
        # print(user1.posts[0].content)
        # print(user1.posts[0].post_type)
        # print(user1.posts[1].content)
        # print(user1.posts[1].post_type)

    def get_follower_count(self):
        return len(self.followers)

        # user1.follow(user3)
        # print(user3.get_follower_count())

    def get_following_count(self):
        return len(self.following)
    
        # user1.follow(user3)
        # print(user1.get_following_count())
    
    def get_recent_posts(self, days=7):
        current_time = datetime.datetime.now()
        recent_posts = []
        for post in self.posts:
            if post.timestamp >= current_time - datetime.timedelta(days=days):
                recent_posts.append(post)
        return recent_posts

        #Untested
    
    def can_view_profile(self, viewer_user):
        if self.is_private == False:
            return True
        elif self.is_private == True and viewer_user in self.following:
            return True
        else:
            return False
        
        # user1.is_private = True
        # user2.follow(user1)
        # print(user2.can_view_profile(user1))
    
    def get_mutual_followers(self, other_user):
        mutuals = []
        for user in self.followers:
            if user in other_user.followers:
                mutuals.append(user)
        return mutuals
    
        # user1.follow(user2)
        # user3.follow(user2)
        # user4.follow(user2)
        # user1.follow(user5)
        # user2.follow(user5)
        # user3.follow(user5)

        # mutuals = user2.get_mutual_followers(user5)
        # for user in mutuals:
        #   print(user.username)
    
    def get_activity_level(self):
        recent_posts = self.get_recent_posts()
        if len(recent_posts) >= 7:
            return "high"
        elif len(recent_posts) >= 2:
            return "medium"
        else:
            return "low"
        
        # user1.create_post("My first post!")
        # user1.create_post("My second post!")
        # user1.create_post("My third post!")
        # user1.create_post("My fourth post!")
        # user1.create_post("My fifth post!")
        # user1.create_post("My sixth post!")
        # user1.create_post("My seventh post!")
        # print(user1.get_activity_level())
    
    def block_user(self, user_to_block):
        self.blocked_users.append(user_to_block)

        # user1.block_user(user2)
        # for user in user1.blocked_users:
        #     print(user.username)
    
    def is_blocked(self, other_user):
        if other_user in self.blocked_users:
            return True
        else:
            return False

        # user1.block_user(user2)
        # print(user1.is_blocked(user2))
    
    def get_post_count(self):
        return len(self.posts)
    
        # user1.create_post("My first post")
        # user1.create_post("My second post")
        # print(user1.get_post_count())
    
    def get_average_post_engagement(self):
        total = 0
        for post in self.posts:
            total += len(post.likes) + len(post.comments)
        return total / len(self.posts)
            
        # user1.create_post("My name is Jack. #swag")
        # user1.create_post("My second post!")
        # user1.posts[0].add_comment(user2, "So swag")
        # user1.posts[0].add_comment(user2, "You had so much swag that day")
        # user1.posts[0].like(user2)
        # user1.posts[1].like(user3)
        # user1.posts[1].add_comment(user3, "Swag!")
        # print(user1.get_average_post_engagement())

class Post:
    def __init__(self, author, content, post_type):
        self.author = author
        self.content = content
        self.post_type = post_type
        self.timestamp = datetime.datetime.now()
        self.likes = []
        self.comments = []
        self.is_edited = False
        self.view_count = 0
    
    def like(self, user):
        if user in self.likes:
            pass
        else:
            self.likes.append(user)
        
        # user1.create_post("My post")
        # user1.posts[0].like(user2)
        # user1.posts[0].like(user2)
        # user1.posts[0].like(user3)
        # for like in user1.posts[0].likes:
        #     print(like.username)

    def unlike(self, user):
        if user in self.likes:
            self.likes.remove(user)
        
        # user1.create_post("My post")
        # user1.posts[0].like(user2)
        # user1.posts[0].like(user3)
        # user1.posts[0].unlike(user2)
        # for like in user1.posts[0].likes:
        #     print(like.username)
    
    def add_comment(self, user, comment_text):
        self.comments.append(Comment(user, comment_text, self))

        # user1.create_post("My name is Jack.")
        # print(user1.posts[0].content)
        # user1.posts[0].add_comment(user2, "Hi Jack, I am Paige.")
        # user1.posts[0].add_comment(user3, "Hi Jack, I am Will.")

        # for comment in user1.posts[0].comments:
        #     print(comment.content)
    
    def get_like_count(self):
        return len(self.likes)

        # user1.create_post("My name is Jack.")
        # user1.posts[0].like(user2)
        # user1.posts[0].like(user3)
        # user1.posts[0].like(user4)
        # print(user1.posts[0].get_like_count())
    
    def get_engagement_score(self):
        return len(self.likes) + len(self.comments) + self.view_count

        # user1.create_post("My name is Jack.")
        # user1.posts[0].like(user2)
        # user1.posts[0].add_comment(user2, "Hi Jack, I am Paige.")
        # print(user1.posts[0].get_engagement_score())
    
    def is_trending(self):
        if self.get_engagement_score() > 2:
            return True
        else:
            return False
        
        # user1.create_post("My name is Jack.")
        # user1.posts[0].like(user2)
        # user1.posts[0].like(user3)
        # user1.posts[0].add_comment(user2, "Hi Jack, I am Paige.")
        # print(user1.posts[0].is_trending())
    
    def get_top_comments(self, limit=3):
        self.comments.sort(key=lambda comment: len(comment.likes), reverse=True)
        return self.comments[:limit] 
    
        # user1.create_post("My name is Jack.")
        # user1.posts[0].add_comment(user2, "Hi Jack, I am Paige.")
        # user1.posts[0].add_comment(user3, "Hi Jack, I am Will.")
        # user1.posts[0].add_comment(user5, "Hi Jack, I am Eric.")
        # user1.posts[0].comments[2].like(user2)
        # user1.posts[0].comments[2].like(user4)
        # user1.posts[0].comments[2].like(user5)
        # user1.posts[0].comments[1].like(user2)
        # user1.posts[0].comments[1].like(user3)
        # user1.posts[0].comments[0].like(user3)

        # for comment in user1.posts[0].comments:
        #     print(f"{comment.content} | Likes: {len(comment.likes)}")
        # top_comments = user1.posts[0].get_top_comments()
        # for comment in top_comments:
        #     print(comment.content)

    def has_hashtags(self):
        words = self.content.split()
        for word in words:
            if word.startswith('#') and len(word) > 1:
                return True
        return False

        # user1.create_post("My name is Jack. #swag")
        # print(user1.posts[0].has_hashtags())
    
    def extract_hashtags(self):
        hashtags = []
        words = self.content.split()
        for word in words:
            if word.startswith('#') and len(word) > 1:
                hashtags.append(word)
        return hashtags

        # user1.create_post("My name is Jack. #swag #yolo #412 !@#$")
        # hashtags = user1.posts[0].extract_hashtags()
        # for hashtag in hashtags:
        #     print(hashtag)
    
    def get_age_in_days(self):
        current_time = datetime.datetime.now()
        days = current_time - self.timestamp
        return days.days
        
        # Untested
    
    def edit_content(self, new_content):
        self.content = new_content
        self.is_edited = True

        # user1.create_post("My name is Jack. #swag #yolo #412 !@#$")
        # print(user1.posts[0].is_edited)
        # user1.posts[0].edit_content("My name is Jack")
        # print(user1.posts[0].content)
        # print(user1.posts[0].is_edited)

class Comment:
    def __init__(self, author, content, parent_post):
        self.author = author
        self.content = content
        self.parent_post = parent_post
        self.timestamp = datetime.datetime.now()
        self.likes = []
        self.replies = []
    
    def like(self, user):
        if user in self.likes:
            pass
        else:
            self.likes.append(user)
    
    def unlike(self, user):
        if user in self.likes:
            self.likes.remove(user)
    
    def add_reply(self, user, reply_text):
        self.replies.append(Comment(user, reply_text, self))

        # user1.create_post("My name is Jack. #swag")
        # user1.posts[0].add_comment(user2, "So swag")
        # user1.posts[0].comments[0].add_reply(user3, "So so swag")

        # print(user1.posts[0].content)
        # print(user1.posts[0].comments[0].content)
        # print(user1.posts[0].comments[0].replies[0].content)
    
    def get_like_count(self):
        return len(self.likes)
    
        # user1.create_post("My name is Jack. #swag")
        # user1.posts[0].add_comment(user2, "So swag")
        # user1.posts[0].comments[0].like(user2)
        # user1.posts[0].comments[0].like(user3)
        # print(user1.posts[0].comments[0].get_like_count())
    
    def get_reply_count(self):
        return len(self.replies)
    
        # user1.create_post("My name is Jack. #swag")
        # user1.posts[0].add_comment(user2, "So swag")
        # user1.posts[0].comments[0].add_reply(user2, "So so swag")
        # user1.posts[0].comments[0].add_reply(user3, "So so so swag")
        # print(user1.posts[0].comments[0].get_reply_count())
    
    def get_total_engagement(self):
        total = self.get_like_count()
        for reply in self.replies:
            total += reply.get_like_count()
        return total

        # user1.create_post("My name is Jack. #swag")
        # user1.posts[0].add_comment(user2, "So swag")
        # user1.posts[0].comments[0].like(user2)
        # user1.posts[0].comments[0].add_reply(user2, "So so swag")
        # user1.posts[0].comments[0].replies[0].like(user1)
        # print(user1.posts[0].comments[0].get_total_engagement())
    
    def is_by_post_author(self):
        if self.parent_post.author == self.author:
            return True
        else:
            return False
        
        # user1.create_post("My name is Jack. #swag")
        # user1.posts[0].add_comment(user2, "So swag")
        # user1.posts[0].add_comment(user1, "I had so much swag that day")
        # print(user1.posts[0].comments[0].is_by_post_author())
        # print(user1.posts[0].comments[1].is_by_post_author())

class SocialNetwork:
    def __init__(self, platform_name):
        self.platform_name = platform_name
        self.users = {}
        self.all_posts = []
    
    def register_user(self, username, email, bio):
        self.users.update({username:User(username, email, bio)})

        # network1 = SocialNetwork("Jackchat")
        # network1.register_user("jack", "jack@email.com", "My name is Jack!")
        # network1.register_user("paige", "paige@email.com", "My name is Paige!")
        # network1.register_user("will", "will@email.com", "My name is Will!")
        # network1.register_user("krista", "krista@email.com", "My name is Krista!")
        # network1.register_user("eric", "eric@email.com", "My name is Eric!")

        # for user in network1.users:
        #     print(user)

    def find_user(self, username):
        found_user = ""
        for user in self.users:
            if username.lower() == user.lower():
                found_user = user
                break
        if found_user == "":
            return None
        else:
            return found_user
        
        ## Used for login username lookup
        # network1 = SocialNetwork("Jackchat")
        # network1.register_user("jack", "jack@email.com", "My name is Jack!")
        # print(network1.find_user("jack"))

    def search_users(self, username):
        results = []
        for user in self.users:
            if username.lower() in user.lower():
                results.append(user)
        return results

        ## Used for partial matching
        # print(network1.search_users("a"))
    
    def get_trending_posts(self, limit=10):
        all_posts_with_scores = []
        sorted_posts = []
        for key, value in self.users.items():
            for post in value.posts:
                all_posts_with_scores.append((post, post.get_engagement_score()))
        all_posts_with_scores.sort(key=lambda item: item[1], reverse=True)
        for post in all_posts_with_scores:
            sorted_posts.append(post[0])
        return sorted_posts[:limit]

        # network1.users["jack"].create_post("I am Jack")
        # network1.users["paige"].create_post("I am paige")
        # network1.users["will"].create_post("I am will")
        # network1.users["krista"].create_post("I am krista")
        # network1.users["eric"].create_post("I am eric")

        # network1.users["jack"].posts[0].like("eric")
        # network1.users["jack"].posts[0].like("paige")
        # network1.users["jack"].posts[0].like("will")
        # network1.users["jack"].posts[0].like("krista")

        # network1.users["paige"].posts[0].add_comment("eric", "nice")
        # network1.users["paige"].posts[0].like("krista")
        # network1.users["paige"].posts[0].like("will")

        # network1.users["eric"].posts[0].like("jack")
        # network1.users["krista"].posts[0].like("jack")


        # for post in network1.get_trending_posts():
        #     print(post.content)
    
    def get_user_feed(self, user, limit=20):
        feed_list = []
        chronological_list = []
        for following in self.users[user].following:
            for post in following.posts:
                if post.get_engagement_score() >= 5:
                    feed_list.append(post)
        feed_list.sort(key=lambda post: post.get_engagement_score(), reverse=True)
        for following in self.users[user].following:
            for post in following.posts:
                if post not in feed_list:
                    chronological_list.append(post)
        chronological_list.sort(key=lambda post: post.timestamp, reverse=True)
        feed_list += chronological_list
        return feed_list[:limit]
    
    # network1.users["jack"].follow(network1.users["paige"])
    # network1.users["jack"].follow(network1.users["will"])
    # network1.users["jack"].follow(network1.users["eric"])

    # network1.users["jack"].create_post("I am Jack")
    # network1.users["eric"].create_post("I drive a BMW")
    # network1.users["paige"].create_post("I am paige")
    # network1.users["will"].create_post("I am will")
    # network1.users["will"].create_post("I am a nurse")
    # network1.users["paige"].create_post("I go to Penn State")
    # network1.users["krista"].create_post("I am krista")
    # network1.users["eric"].create_post("I am eric")

    # network1.users["will"].posts[0].like("jack")
    # network1.users["will"].posts[0].like("will")
    # network1.users["will"].posts[0].like("paige")
    # network1.users["will"].posts[0].like("eric")
    # network1.users["will"].posts[0].like("krista")

    # for post in network1.get_user_feed("jack"):
    #     print(f"{post.author.username} | {post.content}")

    def search_posts(self, keyword):
        results = []
        for username, user in self.users.items():
            for post in user.posts:
                if keyword.lower() in post.content.lower():
                    results.append(post)
        results.sort(key=lambda post: post.get_engagement_score(), reverse=True)
        return results[:20]

        # network1.users["jack"].create_post("I am Jack.")
        # network1.users["paige"].create_post("I am Paige.")
        # network1.users["will"].create_post("I am Will.")
        # network1.users["krista"].create_post("I am Krista.")
        # network1.users["eric"].create_post("I am Eric.")
        # network1.users["jack"].create_post("I went to Penn State.")
        # network1.users["paige"].create_post("I go to Penn State.")
        # network1.users["will"].create_post("I went to IUP.")
        # network1.users["eric"].create_post("I went to IUP.")
        # network1.users["krista"].create_post("I went to IUP.")

        # network1.users["krista"].posts[1].like("eric")
        # network1.users["krista"].posts[1].like("jack")
        # network1.users["eric"].posts[1].like("jack")


        # search_results = network1.search_posts("IUP")
        # for post in search_results:
        #     print(f"{post.author.username} | {post.content}")

    def get_suggested_users(self, user, limit=5):
        suggested_users = []
        for username, other_user in self.users.items():
            if user == other_user:
                continue
            else:
                if len(user.get_mutual_followers(other_user)) > 2:
                    suggested_users.append(other_user)
        suggested_users.sort(key=lambda user: user.get_mutual_followers(other_user), reverse=True)
        return suggested_users[:limit]

        # network1.users["jack"].follow(network1.users["krista"])
        # network1.users["paige"].follow(network1.users["krista"])
        # network1.users["will"].follow(network1.users["krista"])
        # network1.users["jack"].follow(network1.users["eric"])
        # network1.users["paige"].follow(network1.users["eric"])
        # network1.users["will"].follow(network1.users["eric"])
        # for user in network1.get_suggested_users(network1.users["eric"]):
        #     print(user.username)
    
    def get_platform_stats(self):
        total_posts = 0
        total_engagement_score = 0
        for username, user in self.users.items():
            for post in user.posts:
                total_posts += 1
                total_engagement_score += post.get_engagement_score()

        return len(self.users), total_posts, total_engagement_score

        # network1.users["jack"].create_post("I am Jack")
        # network1.users["paige"].create_post("I am paige")
        # network1.users["will"].create_post("I am will")
        # network1.users["krista"].create_post("I am krista")
        # network1.users["eric"].create_post("I am eric")

        # network1.users["jack"].posts[0].like("eric")
        # network1.users["jack"].posts[0].like("paige")
        # network1.users["jack"].posts[0].like("will")
        # network1.users["jack"].posts[0].like("krista")

        # network1.users["paige"].posts[0].add_comment("eric", "nice")
        # network1.users["paige"].posts[0].like("krista")
        # network1.users["paige"].posts[0].like("will")

        # network1.users["eric"].posts[0].like("jack")
        # network1.users["krista"].posts[0].like("jack")

        # users, posts, engagement = network1.get_platform_stats()
        # print(f"Platform has {users} users, {posts} posts, {engagement} total engagement")
    
    def get_most_active_users(self, limit=10):
        active_users = []
        for username, user in self.users.items():
            if len(user.get_recent_posts()) >= 1:
                active_users.append(user)
        active_users.sort(key=lambda user: len(user.get_recent_posts()), reverse=True)
        return active_users[:limit]

        # network1.users["jack"].create_post("I am Jack.")
        # network1.users["jack"].create_post("I made Jackgram.")
        # network1.users["paige"].create_post("I am Paige.")
        # network1.users["will"].create_post("I am Will.")
        # network1.users["krista"].create_post("I am Krista.")
        # network1.users["eric"].create_post("I am Eric.")
        # network1.users["jack"].create_post("I went to Penn State.")
        # network1.users["paige"].create_post("I go to Penn State.")

        # for user in network1.get_most_active_users():
        #     print(user.username, len(user.get_recent_posts()))
    
    def get_hashtag_trends(self):
        all_hashtags = {}
        for username, user in self.users.items():
            for post in user.posts:
                post_hashtags = post.extract_hashtags()
                for hashtag in post_hashtags:
                    if hashtag in all_hashtags:
                        all_hashtags[hashtag] += 1
                    else:
                        all_hashtags[hashtag] = 1
        return sorted(all_hashtags.items(), key=lambda x: x[1], reverse=True)
    
        # network1.users["jack"].create_post("I am Jack. #swag #Lola")
        # network1.users["jack"].create_post("I made Jackgram. #swag #Lola")
        # network1.users["paige"].create_post("I am Paige. #Lola")
        # network1.users["will"].create_post("I am Will. #NURSE")
        # network1.users["krista"].create_post("I am Krista. #Lola")
        # network1.users["eric"].create_post("I am Eric. #BMW")
        # network1.users["jack"].create_post("I went to Penn State. #PSU")
        # network1.users["paige"].create_post("I go to Penn State. #PSU")


        # print(network1.get_hashtag_trends())
    
    def moderate_content(self, post):
        if profanity.contains_profanity(post.content):
            self.users[post.author.username].posts.remove(post)

        # for post in network1.users["jack"].posts:
        #     network1.moderate_content(network1.users["jack"].posts[network1.users["jack"].posts.index(post)])

        # for post in network1.users["jack"].posts:
        #     print(post.content)
    
    def get_user_statistics(self, user):
        engagement_count = 0
        for post in user.posts:
            engagement_count += len(post.likes) + len(post.comments)
        return {"Post count": user.get_post_count(), "Followers": user.get_follower_count(), "Engagements": engagement_count}
    
        # for username, user_object in self.users.items():
        #     for post in user_object.posts:
        #         for like in post.likes:
        #             if like.user == user:
        #                 engagement_count += 1
        #                 break
        #         for comment in post.comments:
        #             if comment.author == user:
        #                 engagement_count += 1

        # network1.users["eric"].follow(network1.users["jack"])
        # network1.users["krista"].follow(network1.users["jack"])
        # network1.users["jack"].create_post("I am Jack.")
        # network1.users["jack"].create_post("I went to Penn State.")
        # network1.users["jack"].posts[0].add_comment("paige", "Same")
        # network1.users["jack"].posts[0].like("paige")

        # print(network1.get_user_statistics(network1.users["jack"]))
    
    def find_influencers(self, min_followers=1000):
        influencers = []
        for username, user in self.users.items():
            if user.get_follower_count() >= min_followers:
                influencers.append(user)
        influencers.sort(key=lambda user: user.get_follower_count(), reverse=True)
        return influencers

        # network1.users["jack"].follow(network1.users["paige"])
        # network1.users["eric"].follow(network1.users["paige"])
        # network1.users["will"].follow(network1.users["paige"])
        # network1.users["krista"].follow(network1.users["paige"])

        # network1.users["jack"].follow(network1.users["will"])
        # network1.users["eric"].follow(network1.users["will"])
        # network1.users["krista"].follow(network1.users["will"])

        # network1.users["jack"].follow(network1.users["eric"])
        # network1.users["paige"].follow(network1.users["eric"])

        # network1.users["paige"].follow(network1.users["krista"])

        # for user in network1.find_influencers(3):
        #     print(f"{user.username} | {user.get_follower_count()}")
    
    def get_daily_active_users(self, date):
        active_users = 0
        for username, user in self.users.items():
            for post in user.posts:
                if post.timestamp.date() == date:
                    active_users += 1
                    break
        return active_users

        # network1.users["jack"].create_post("I am Jack.")
        # network1.users["paige"].create_post("I am Paige.")
        # network1.users["jack"].create_post("I went to Penn State.")

        # print(network1.get_daily_active_users(datetime.date.today()))
        # print(network1.get_daily_active_users(datetime.date(2025, 8, 28)))