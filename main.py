#Description: This program will predict if the stock price of a company will change according to
#             top news headlines. 
#             The Sentiment_Table program was based on a guide I found
#             and the other functions were things I created to help direct the output of Sentiment
#             Analysis into something usable later.

# import urllib.error
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
# import matplotlib.pyplot as plt
# %matplotlib inline
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import datetime, date

#This program will return a table of a given stock's sentiment for every article it could web scrape,
#For larger companies like amazon this goes back to about 6 days of articles
def Sentiment_Table():

  finviz_url = 'https://finviz.com/quote.ashx?t='
  stock_name = input("Enter the letter code for the stock you'd like to see: ")
  full_url = finviz_url + stock_name
  req = Request(url=full_url,headers={'user-agent': 'sentiment-news/0.0.1'})
  response = urlopen(req)
  html_contents = BeautifulSoup(response)
  headline_table = html_contents.find(id='news-table')

  parsed_news = []
  date = ""
  for x in headline_table.findAll('tr'):
    # I think each x is the full tr entry, the .a is a formatting thing, gets
    # rid of some random characters because splits from a href
    text = x.a.get_text()
    # splits text from td tags into a list
    date_scrape = x.td.text.split()
    # when length is one time is the only element
    if len(date_scrape) == 1:
      time = date_scrape[0]
      # otherwise date is the 1st element and time is the second    
    else:
      date = date_scrape[0]
      time = date_scrape[1]
      # Put date, time and headline as a list to the parsed_news list
    parsed_news.append([date, time, text])
  vader = SentimentIntensityAnalyzer()
  columns = ['date', 'time', 'headline']
  parsed_and_scored_news = pd.DataFrame(parsed_news, columns=columns)
  scores = map(vader.polarity_scores, parsed_and_scored_news['headline'])
  scores_df = pd.DataFrame(scores)
  list1 = [parsed_and_scored_news, scores_df]
  parsed_and_scored_news = pd.concat(list1, axis=1)
  parsed_and_scored_news['date'] = pd.to_datetime(parsed_and_scored_news['date'])
  #--> makes it into a date object so date is read differently in the chart
  return parsed_and_scored_news
#test
# Sentiment_Table()

#This program will return all the scores for articles of a given day
def single_day(df = pd.DataFrame, date1 = date):
  datestring = date1.strftime('%m-%d-%Y')
  df_new = df[df['date'] == datestring]
  return df_new['compound']

#test
# datetest = date(2021, 8, 5)
# parsed_and_scored_news = Sentiment_Table()
# single_day(parsed_and_scored_news, datetest)

#This program will find the overall sentiment for a given day based on all the sentiment scores for articles for that day
def totalcompound(ser1 = pd.Series):
  maxval = ser1.max()
  minval = ser1.min()
  if minval > 0:
    minval = 0
  if maxval < 0:
    maxval = 0
  return round(minval + maxval, 4)

#test
# datetest = date(2021, 8, 5)
# parsed_and_scored_news = Sentiment_Table()
# z = single_day(parsed_and_scored_news, datetest)
# totalcompound(z)