import requests
from bs4 import BeautifulSoup
import re
import csv


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


def parse_page_content(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    
    # Find the football-fixtures container
    fixtures = soup.find('section', class_='matchesCenter')
    
    # Find all championships within the fixtures container
    championships = fixtures.find_all('div', class_=re.compile(r'matchCard matchesList'))
    
    matches_list = []  # List to store all match data
    
    # Loop through championships to extract data for each championship
    for championship in championships:
        
        # Find championship title
        championship_title = championship.find('div', class_='title').h2.text.strip()
        
        # Find all matches for each championship
        matches = championship.find_all('div', class_='allData')
        
        # Loop through matches and extract their details
        for match in matches:
            match_dic = {}  # Dictionary to store match details
            
            match_dic['الفريق الأول'] = match.find('div', class_='teams teamA').p.text.strip()
            result = match.find_all('span', class_='score')
            match_dic['نتيجة المباراة'] = f"{result[1].text.strip()} - {result[0].text.strip()}"
            match_dic['الفريق الثاني'] = match.find('div', class_='teams teamB').p.text.strip()
            match_dic['الحالة'] = match.find('div', class_='matchStatus').span.text.strip()
            match_dic['موعد المباراة'] = match.find('span', class_='time').text.strip()
            match_dic['رقم الجولة'] = match.find('div', class_='date').text.strip()
            match_dic['البطولة'] = championship_title

            matches_list.append(match_dic)  # Append the match dictionary to the list
    
    return matches_list  # Returns a list of dictionaries for all matches


def save_to_csv(data):
    with open('football_fixtures.csv', 'w', encoding='utf-8') as f:
        # Define the desired fieldnames for the CSV file
        fieldnames = ['الفريق الأول', 'نتيجة المباراة', 'الفريق الثاني', 'الحالة', 'موعد المباراة', 'رقم الجولة', 'البطولة']
        
        # Create the CSV DictWriter object
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        # Write the header row
        csv_writer.writeheader()
        
        # Write each row to the CSV file
        csv_writer.writerows(data)
        


if __name__ == '__main__':
    football_page_url = "https://www.yallakora.com/match-center/?date=10/12/2024"
    
    # Fetching (requesting) football page
    football_page = fetch_page_content(football_page_url)
    
    # Parsing (extracting) football data
    football_data = parse_page_content(football_page)
    
    save_to_csv(football_data)
    
    
    