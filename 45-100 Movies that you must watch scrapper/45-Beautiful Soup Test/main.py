
# Script that scrape data from website.html using BeautifulSoup. I used html anchor
import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

articles = soup.find_all("span", class_="titleline")
article_text = []
article_link = []

for article_tag in articles:
    text = article_tag.getText()
    article_text.append(text)
    link = article_tag.find("a").get("href")
    article_link.append(link)

article_upvote = []
for score in soup.find_all("span", class_="score"):
    score = int((score.getText()).split()[0])
    article_upvote.append(score)

max_score = max(article_upvote)
max_score_index = article_upvote.index(max_score)

# print(article_text) 
# print(article_link)
# print(article_upvote)

print(article_text[max_score_index]) 
print(article_link[max_score_index])
print(article_upvote[max_score_index])
