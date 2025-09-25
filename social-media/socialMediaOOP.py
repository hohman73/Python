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
