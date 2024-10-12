import praw
import time



# Authenticate with Reddit API using PRAW
reddit = praw.Reddit(
    username="Geniusrover",
    client_id="6nFDVDkA-bp91Q7W_m6htw",
    client_secret="dT3fhjopzPpOwiCpjJp82d8WwNszwA",
    user_agent="InsightScoutBot by u/Geniusrover"
)



# Define keywords and product recommendations for the bot
PRODUCT_KEYWORDS = {
    "app to identify names in pictures": "I recommend using [FaceApp](https://example.com/faceapp), a great face recognition tool.",
    "AI tool for writing": "You might want to try [OpenAI's ChatGPT](https://openai.com/chatgpt), an AI tool for writing assistance.",
    "best budget smartphone": "Consider checking out the [XYZ Smartphone](https://example.com/smartphone) for the best budget performance."
}

# Define a function to reply to comments
def reply_to_comment(comment, reply_text):
    try:
        comment.reply(reply_text)
        print(f"Replied to comment ID: {comment.id}")
    except Exception as e:
        print(f"Error replying to comment ID: {comment.id}, error: {e}")

#define the main behaviour of the bot;

def run_bot(time_limit_seconds=60):
    subreddit = reddit.subreddit("all")  # Targeting all subreddits for broad reach
    start_time = time.time()  # Record the start time

    for comment in subreddit.stream.comments(skip_existing=True):
        current_time = time.time()  # Get the current time
        elapsed_time = current_time - start_time  # Calculate the elapsed time

        if elapsed_time >= time_limit_seconds:
            print(f"Time limit of {time_limit_seconds} seconds reached. Stopping bot.")
            break
        
        print(f"AskReddit comment found: {comment.body}")
        print(f"Comment found: {comment.body}")

        # Reply to questions with relevant answers
        if "advice" in comment.body.lower() or "help" in comment.body.lower():
            reply_to_comment(comment, "Hi! I'm GeniusRover. How can I assist you today?")

        # Promote products based on user queries
        for keyword, product_reply in PRODUCT_KEYWORDS.items():
            if keyword in comment.body.lower():
                reply_to_comment(comment, product_reply)

        # Like and repost valuable comments
        if len(comment.body.split()) > 50:  # Example heuristic: If the comment is long and detailed
            try:
                comment.upvote()
                print(f"Upvoted comment ID: {comment.id}")
            except Exception as e:
                print(f"Error upvoting comment ID: {comment.id}, error: {e}")

            try:
                comment.submission.reply(f"This comment is worth highlighting: {comment.body}")
                print(f"Reposted comment ID: {comment.id}")
            except Exception as e:
                print(f"Error reposting comment ID: {comment.id}, error: {e}")

        time.sleep(2)  # To avoid API rate-limiting

# Run the bot with a time limit
if __name__ == "__main__":
    run_bot(time_limit_seconds=300)  # Set the desired time limit in seconds (e.g., 300 seconds = 5 minutes)
