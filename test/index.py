import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
website = requests.get(url)
soup = BeautifulSoup(website.text, "html.parser")
quote = soup.select('.text')
print(quote)
