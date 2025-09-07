import tweepy
import json


API_KEY = "JQCmBGkFZmbeO8nZDG8emVQLT"
API_SECRET_KEY = "pos3uTIQMWB8dwlAf0TApagEbPpXyYXZMp4pcHYxuEV4Gn0TiR"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAAN33gEAAAAAFTspkv610bnPgd0HL0D1hQtg7g0%3DhPOlFV2B6EVUGZ4h5GtuJx9J1lU3ttJEv3H6qNtybUOtQp566C"
ACCESS_TOKEN = "1956984986965577728-VXdEiYDb38fliQpr9wu3hhfTvFIY1K"
ACCESS_TOKEN_SECRET = "afBKKnJRnAoCJGqvmuDvdxyD8ogE7JWnUo9BzOETcEAmG"



if __name__ == "__main__":
    try:
        twitterClient = tweepy.Client(
            bearer_token=BEARER_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET,
            consumer_key=API_KEY,
            consumer_secret=API_SECRET_KEY,
            access_token=ACCESS_TOKEN,
            wait_on_rate_limit=True,
        )

        user = twitterClient.get_user(username="sundarpichai")

        user_id = user.data.id

        # get tweets
        tweets  = twitterClient.get_users_tweets(
            user_id,
            max_results=50, # for people who got the output -> 50
            tweet_fields=['created_at', 'public_metrics', 'text']
        )

        # save the tweets to json file
        with open("extracted_tweets.json", "w") as json_file:
            # [].map(e=>e.toString())
            json.dump([tweet.data for tweet in tweets.data], json_file, indent=4)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")