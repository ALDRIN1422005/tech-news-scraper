import requests
from bs4 import BeautifulSoup

URL = "https://techcrunch.com"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

headlines = soup.find_all('a', class_='post-block__title__link')

print("Top Tech Headlines from TechCrunch:")
for h in headlines[:5]:
    print("-", h.get_text().strip())
