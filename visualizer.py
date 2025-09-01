import matplotlib.pyplot as plt
import pandas as pd

def plot_sentiment_distribution(df):
    plt.figure(figsize=(6,4))
    top_sentiments = df['Sentiment'].value_counts().head(10)
    top_sentiments.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Sentiment Distribution")
    plt.ylabel("")
    plt.savefig("sentiment_distribution.png")
    plt.show()

def plot_year_distribution(df):
    plt.figure(figsize=(6,4))
    df['Year'].value_counts().plot(kind='bar')
    plt.title("Number of Posts from 2010 to 2023")
    plt.xlabel("Years")
    plt.ylabel("Number of Posts")
    plt.savefig("year_distribution.png")
    plt.show()

def plot_country_distribution(df):
    plt.figure(figsize=(6,4))
    top_sentiments = df['Country'].value_counts().head(10)
    top_sentiments.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Country Distribution")
    plt.ylabel("")
    plt.savefig("country_distribution.png")
    plt.show()
