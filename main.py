import praw
import datetime

# إعداد الاتصال بـ Reddit API
reddit = praw.Reddit(
    client_id="af6z486yb_P9hLIEubRb7g",
    client_secret="X7bGAvYvybhNSy6MMVQdp4amYXdXyw",
    username="mohammedbj",
    password="Mm123321",
    user_agent="my_reddit_bot_v1"
)

# جلب بوست عشوائي من r/AskReddit
subreddit = reddit.subreddit("AskReddit")
post = next(subreddit.hot(limit=10))

print("✅ تم الاتصال بـ Reddit")
print("📝 عنوان البوست:", post.title)
print("💬 محتوى البوست:", post.selftext)
print("🔗 الرابط:", f"https://www.reddit.com{post.permalink}")
print("🕒 الوقت:", datetime.datetime.now())
