import requests

quote = requests.get("https://api.kanye.rest/").json()["quote"]

