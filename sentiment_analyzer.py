import pandas as pd

def analyze_sentiment(df):
        print(df[['Text', 'Sentiment', 'Year']].head(10))
        print(f"The total posts are {len(df)} posts.")
        print(f"There are {len(df[df['Sentiment'].str.strip() == 'Positive'])} positive posts.")
        print(f"There are {len(df[df['Year'] == 2023])} posts in 2023.")
        print(f"There are {len(df[df['Country'].str.strip() == 'UK'])} posts from United Kingdom.")
        print(f"The average retweets is {df['Retweets'].mean():.2f} and average likes is {df['Likes'].mean():.2f}.")
        

def save_sentiment_report(df, filename="sentiment_report.csv"):
    try:
        df.to_csv(filename, index=False)
        print(f"Sentiment report saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")
