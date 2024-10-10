import requests
from bs4 import BeautifulSoup

page_url = "https://www.yallakora.com/match-center/?date=10/10/2024"


def fetch_page_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }
    
    try:
        page = requests.get(url, headers=headers, timeout=5)
        page.raise_for_status()  # Raises an error for non-successful requests
        return page.content  # Return HTML page content
    
    except requests.exceptions.HTTPError as http_error:
        print(f"HTTP error occurred: {http_error}")
    except requests.exceptions.Timeout as timeout_error:
        print(f"Timeout error occurred: {timeout_error}")
    except requests.exceptions.ConnectionError as connect_error:
        print(f"Connection error occurred: {connect_error}")
    except requests.exceptions.RequestException as error:
        print(f"An error occurred: {error}")
    return None


fetch_page_content(page_url)
