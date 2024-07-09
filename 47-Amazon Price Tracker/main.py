
# to check my http heardes go to this link https://myhttpheader.com/
import smtplib
import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

rs = requests.get(url, headers={"User-Agent":"Defined"})
soup= BeautifulSoup(rs.text, "html.parser")

title = soup.find("h1", id="title").getText()
title = " ".join(title.split())
price = soup.find("span", class_="a-offscreen").getText()
price = float(price.replace("$", ""))

print(title)
print(price)
content = f"{title}\n is now ${price}"

s = smtplib.SMTP('smtp.gmail.com', 587) # creates SMTP session
s.starttls() # start TLS for securit

sender_email = "YOUR_EMAIL@gmail.com"
sender_password = "YOUR_APP_PASSWORD"
s.login(sender_email, sender_password)# Authentication

msg = f"Subject:Test-Amazon Pricer alert!\n\n{content}\n{url}"
sender_email_id = "YOUR_EMAIL@gmail.com"
receiver_email_id = "YOUR_EMAIL@gmail.com"
s.sendmail("sender_email_id", "receiver_email_id", msg)
s.quit()