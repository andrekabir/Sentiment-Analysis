DESCRIPTION

This is a program designed to capture the sentiment of news headlines and use that to say if a stock is a buy, hold, or sell for a given day. This project is not meant to be an accurate predictor and is just a tool I am using to learn new things, and to have fun. More will be added to this repository as this is a component of a larger machine learning project I am doing with some fellow students.

PACKAGES

The packages involved in this project are:

-> urllib.request: To access the website and access the html of the page for web scraping purposes

-> bs4: To turn the html into a format that is easier to parse

-> pandas: For using dataframes

-> ntlk.sentiment.vader: For analyzing the news headlines and assigning them a score that indicates their positivity or negativity

-> datetime: To handle date input from the date of the articles

COMING SOON

- Producing a graph for each of the days
- Using the ratings provided to mark the stock as a buy, hold, or sell for a certain day
- Routing the error that occurs from entering a stock that does not exist into a loop that runs until the user inputs an actual stock
- Sorting the headlines better by putting stocks into dates according to the time of the headline and how that corresponds with the current or next business day, and not just the day the news articles was released
