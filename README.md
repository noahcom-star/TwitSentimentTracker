# Twitter Sentiment Analyzer 🐦📊

**Twitter Sentiment Analyzer** is a Python-powered application designed to fetch real-time tweets based on user-defined queries, analyze their sentiments, and visualize the results. Whether you're a beginner exploring AI or a data enthusiast interested in social media trends, this tool offers a straightforward way to gauge public opinion on various topics.

## 📌 **Features**

- **Real-Time Tweet Fetching:** Retrieve up to 100 recent tweets based on specific search terms.
- **Data Cleaning:** Preprocess tweets by removing retweets, mentions, URLs, and unnecessary whitespace.
- **Sentiment Analysis:** Utilize TextBlob to determine the polarity of each tweet, categorizing them as positive, neutral, or negative.
- **Visualization:** Generate intuitive bar charts to visualize the distribution of sentiments.
- **Configurable Settings:** Easily adjust parameters like tweet count and sentiment thresholds via a `config.json` file.
- **Debugging Tools:** Option to view cleaned tweets and their polarity scores for deeper insights.

## 🛠 **Technologies Used**

- **Python 3.x**
- **Libraries:**
  - [Tweepy](https://www.tweepy.org/) for interacting with the Twitter API
  - [TextBlob](https://textblob.readthedocs.io/en/dev/) for sentiment analysis
  - [Matplotlib](https://matplotlib.org/) for data visualization
  - **Regex** (`re`) for text preprocessing

## 🚀 **Getting Started**

### **Prerequisites**

- Python 3.x installed on your machine
- Twitter Developer Account with API credentials

### **Installation**

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/twitter-sentiment-analyzer.git
    cd twitter-sentiment-analyzer
    ```

2. **Install Required Libraries:**

    ```bash
    pip install tweepy textblob matplotlib
    ```

3. **Configure API Credentials:**

    - Create a `config.json` file in the root directory.
    - Populate it with your Twitter API credentials and desired settings:

    ```json
    {
        "bearer_token": "YOUR_TWITTER_BEARER_TOKEN",
        "default_tweet_count": 50,
        "polarity_positive_threshold": 0.2,
        "polarity_negative_threshold": -0.2
    }
    ```

### **Usage**

Run the sentiment analyzer script:

```bash
python sentiment_analyzer.py
