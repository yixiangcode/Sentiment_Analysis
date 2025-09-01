import pandas as pd
from data_loader import load_data
from sentiment_analyzer import analyze_sentiment, save_sentiment_report
from visualizer import plot_sentiment_distribution, plot_year_distribution, plot_country_distribution, plot_platform_distribution

file_path = 'Sentiment_Data.csv'

df = load_data(file_path)

analyze_sentiment(df)
save_sentiment_report(df[['Text', 'Sentiment']])
plot_sentiment_distribution(df)
plot_country_distribution(df)
plot_year_distribution(df)
plot_platform_distribution(df)
