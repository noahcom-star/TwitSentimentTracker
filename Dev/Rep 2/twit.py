import json
import tweepy
import re
from textblob import TextBlob
import matplotlib.pyplot as plt

def load_config():
    with open("config.json", "r", encoding="utf-8") as f:
        data = f.read()
        print("File content:", data)  # Debugging: ensure the JSON is read correctly
        return json.loads(data)

def authenticate(config):
    # For v2, we primarily use the bearer token
    # API keys/token below are retained but unused since we fetch tweets via v2 endpoints.
    client = tweepy.Client(bearer_token=config["bearer_token"])
    return client

def fetch_tweets(client, query, count):
    # Twitter API v2: search_recent_tweets can fetch up to 100 tweets per request
    max_results = min(count, 100)
    # Append `lang:en` to the query to filter English tweets
    query = f"{query} lang:en"
    response = client.search_recent_tweets(query=query, max_results=max_results, tweet_fields=['text'])
    return response.data if response.data else []

def preprocess_tweet(text):
    text = re.sub(r'RT\s+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def analyze_sentiment(tweets, pos_threshold, neg_threshold, debug=False):
    positive_count = 0
    neutral_count = 0
    negative_count = 0
    processed_tweets = []

    for tweet in tweets:
        # In v2, tweet.text is always the full text of the tweet
        cleaned_text = preprocess_tweet(tweet.text)
        blob = TextBlob(cleaned_text)
        polarity = blob.sentiment.polarity
        if polarity > pos_threshold:
            positive_count += 1
        elif polarity < neg_threshold:
            negative_count += 1
        else:
            neutral_count += 1
        if debug:
            processed_tweets.append((cleaned_text, polarity))

    return positive_count, neutral_count, negative_count, processed_tweets

def plot_results(positive, neutral, negative):
    labels = ['Positive', 'Neutral', 'Negative']
    counts = [positive, neutral, negative]
    plt.bar(labels, counts, color=['green', 'blue', 'red'])
    plt.title('Sentiment Distribution')
    plt.ylabel('Count')
    plt.show()

def main():
    config = load_config()
    client = authenticate(config)

    query = input("Enter a search term: ")
    count_input = input("Number of tweets to fetch (default: {}): ".format(config["default_tweet_count"]))
    try:
        count = int(count_input) if count_input.strip() else config["default_tweet_count"]
    except ValueError:
        count = config["default_tweet_count"]

    tweets = fetch_tweets(client, query, count)
    positive, neutral, negative, processed = analyze_sentiment(
        tweets,
        pos_threshold=config.get("polarity_positive_threshold", 0.2),
        neg_threshold=config.get("polarity_negative_threshold", -0.2),
        debug=False
    )

    print("Positive:", positive)
    print("Neutral:", neutral)
    print("Negative:", negative)

    show_chart = input("Show chart? (y/n): ")
    if show_chart.lower() == 'y':
        plot_results(positive, neutral, negative)

    debug_print = input("Print cleaned tweets for debugging? (y/n): ")
    if debug_print.lower() == 'y':
        _, _, _, debug_tweets = analyze_sentiment(
            tweets,
            pos_threshold=config.get("polarity_positive_threshold", 0.2),
            neg_threshold=config.get("polarity_negative_threshold", -0.2),
            debug=True
        )
        for t, p in debug_tweets[:10]:
            print(t, "Polarity:", p)

if __name__ == "__main__":
    main()