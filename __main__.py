import requests as req
from bs4 import BeautifulSoup


# PROPERTIES
URL = "https://news.ycombinator.com"

res = req.get(URL).text
soup = BeautifulSoup(res, "html.parser")

vote_arrows = soup.find_all(name="div", class_="votearrow")
headlines = soup.find_all(name="a", class_="storylink")
scores = soup.find_all(name="span", class_="score")

headline_values = [headline.text for headline in headlines]
link_values = [headline.get("href") for headline in headlines]
score_values = [int(score.text.split()[0]) for score in scores]

articles = [{"headline": headline_values[i], "link": link_values[i]} for i in range(10)]


# MAIN
for i, article in enumerate(articles):
    print(f"{i + 1} {article['headline']}: {article['link']}")
