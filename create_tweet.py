import json
from run_prompt import execute_gemini_for_tweet_creation

def create_tweet(analyzed_tweets):
    iphone17_prompt = (
        "Write a tweet for newly releasing iPhone 17 Pro Max with A18 Pro launching "
        "with physically moving camera zoom. "
        "Make this tweet more appealing for camera enthusiast audience."
    )

    system_prompt = f"""
    Create an engaging Twitter tweet for my tech company.
    PROMPT: {iphone17_prompt}

    Here are some example tweets and their sentiment analysis with very high user
    engagements of other similar companies.
    Example Tweets: {analyzed_tweets}

    Create the tweet, compare it with the example tweets and predict and explain why 
    and how this tweet will perform well compared to the given examples.
    """

    print("\n=== SYSTEM PROMPT SENT TO GEMINI ===")
    print(system_prompt)  # 👈 Debug what is sent

    out = execute_gemini_for_tweet_creation(prompt=system_prompt)

    print("\n=== RAW GEMINI OUTPUT ===")
    print(out)  # 👈 Debug what Gemini returns

    try:
        out_dict = json.loads(out)
    except Exception as e:
        print("\n❌ JSON parsing failed:", str(e))
        return

    tweet = out_dict.get("tweet")
    prediction = out_dict.get("prediction")
    explanation = out_dict.get("explanation")

    print("\n===== TWEET =====")
    print(tweet)

    print("\n===== PREDICTION =====")
    print(prediction)

    print("\n===== EXPLANATION =====")
    print(explanation)

    return tweet, prediction, explanation


if __name__ == "__main__":
    with open("analyzed_tweets.json") as f:
        data = json.load(f)
        print("\n=== Tweets loaded ===")
        create_tweet(data)