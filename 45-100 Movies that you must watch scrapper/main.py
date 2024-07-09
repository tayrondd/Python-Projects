import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup= BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("h3", class_="title")
titles_list = []

for title in titles:
    text = title.getText()
    titles_list.append(text)

titles_list.reverse()

with open("top-100.txt", "+w", encoding="utf-8") as file:
    for text in titles_list:
        file.write(text)
        file.write("\n")
        
print("done")