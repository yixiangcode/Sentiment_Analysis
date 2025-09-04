import matplotlib.pyplot as plt
import pandas as pd

def plot_sentiment_distribution(df):
    plt.figure(figsize=(7,4))
    top_sentiments = df['Sentiment'].value_counts().head(15)
    top_sentiments.plot(kind='bar')
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Posts")
    plt.savefig("sentiment_distribution.png")
    plt.show()

def plot_country_distribution(df):
    plt.figure(figsize=(6,4))
    df['Country'] = df['Country'].str.strip().str.lower()
    country_counts = df['Country'].value_counts().head(10)
    country_counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Country Distribution")
    plt.ylabel("")
    plt.savefig("country_distribution.png")
    plt.show()
    
def plot_year_distribution(df):
    plt.figure(figsize=(6,4))
    df['Year'].value_counts().plot(kind='bar')
    plt.title("Number of Posts from 2010 to 2023")
    plt.xlabel("Years")
    plt.ylabel("Number of Posts")
    plt.savefig("year_distribution.png")
    plt.show()

def plot_platform_distribution(df):
    plt.figure(figsize=(6,4))
    df['Platform'] = df['Platform'].str.strip().str.lower()
    platform_counts = df['Platform'].value_counts()
    platform_counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Platform Distribution")
    plt.ylabel("")
    plt.savefig("platform_distribution.png")
    plt.show()

