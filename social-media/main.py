from data import *

for user in network1.users:
    print(user)

for post in network1.get_trending_posts():
    print(post.content)

for post in network1.get_user_feed("jack"):
    print(f"{post.author.username} | {post.content}")

users, posts, engagement = network1.get_platform_stats()
print(f"Platform has {users} users, {posts} posts, {engagement} total engagement")

for user in network1.get_most_active_users():
    print(user.username, len(user.get_recent_posts()))

print(network1.get_hashtag_trends())

print(network1.get_user_statistics(network1.users["jack"]))

for user in network1.find_influencers(3):
    print(f"{user.username} | {user.get_follower_count()}")

print(network1.get_daily_active_users(datetime.date.today()))