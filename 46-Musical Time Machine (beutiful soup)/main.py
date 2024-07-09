import requests
from bs4 import BeautifulSoup

year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

rs = requests.get(f"https://www.billboard.com/charts/hot-100/{year}")
soup= BeautifulSoup(rs.text, "html.parser")

titles = soup.select(selector="li h3", class_="c-title")
titles_list = []

for title in titles:
    text = title.getText().strip()
    titles_list.append(text)

print(titles_list[0:100])

