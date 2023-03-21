from bs4 import BeautifulSoup
from requests_html import HTMLSession

quotes = []
s = HTMLSession()
LASTPAGE = 88 #Last Page on Website
for i in range(1, LASTPAGE):
    URL = f'https://www.goodreads.com/author/quotes/17212.Marcus_Aurelius?page={i}'
    r = s.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.find_all('div', class_='quoteText')
    with open('scraped.txt', 'w', encoding="utf-8") as f:
        for line in data:
            quote = line.text
            f.write(quote)

