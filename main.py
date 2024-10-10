import requests
from bs4 import BeautifulSoup

page_url = "https://www.yallakora.com/match-center/?date=10/10/2024"


def fetch_page_content(url):
    page = requests.get(url)
    
    if page.status_code == 200:
        print(page.content)
    else:
        print("An error occurred")


fetch_page_content(page_url)
