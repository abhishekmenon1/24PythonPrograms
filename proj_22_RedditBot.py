# You can program a bot that monitors subreddits and reports whenever they find something useful.
# It will save Redditors a lot of time and provide helpful information with it.

import praw  # API library used to scape Reddit

reddit = praw.Reddit(                               # information derived from Reddit for Bot account
    client_id="690h7_8ve8Xn4DF6bsQ9uw",
    client_secret="cQ_2CuFz82yMsX92erRLbNwrcxZeAQ",
    user_agent="<console: search for useful info",
)

subreddit = reddit.subreddit("stocks")  # scraping through Stocks subreddit

for sub in subreddit.hot(limit=2):   # no of submission is 10 from "hot" section
    print(sub.title)

    for comment in sub.comments:        # looking for comments for each submission
        if hasattr(comment, "body"):    # checking if the submission has any comments
            comment_lower = comment.body.lower()
            if (" buy " or " good ") in comment_lower:  # searching for "buy" and "good" in the comments
                print(comment.body)                     # printing the comments with "buy" and "good"
                print("----------")
