import requests
from bs4 import BeautifulSoup

AMAZON_URL = "https://www.amazon.in/gp/product/B00NU0JS1O/ref=ox_sc_act_title_1?smid=AT95IG9ONZD7S&psc=1"
AMAZON_HEADER = {
    "Accept-Language": "en-US",
    "User-Agent": "Chrome/96.0.4664.110 Safari/537.36"
}

response = requests.get(url=AMAZON_URL, headers=AMAZON_HEADER)
response.raise_for_status()
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

# Find the amount element
price_span = soup.find(name="span", class_="apexPriceToPay")
print(f"Got the response: {price_span.getText()}")
