from bs4 import BeautifulSoup

with open("website.html", encoding='UTF8') as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "html.parser")

heading = soup.find("h1", id="name")
print(heading.getText())

heading = soup.select(".heading")
print(heading)