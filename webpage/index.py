import requests
from bs4 import BeautifulSoup

website = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(website.text, 'html.parser')
quotes = soup.select('.quote')
for quote in quotes:
	text = quote.select_one('.text')
	author = quote.select_one('.author')
	tags = quote.select('.tag')
	print(text.text)
	print(author.text)
	for tag in tags:
		print(tag.text)
	print('=========================')
