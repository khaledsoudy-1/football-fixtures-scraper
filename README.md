# ⚽ Football Fixtures Scraper

## 📖 Description
A robust Python web scraper that collects football match data from Yallakora for a specified date. The program extracts comprehensive match information including team names, scores, match status, time, round, and championship. It saves the data in a structured CSV format for easy analysis.

## ✨ Features
- Date-specific football match data scraping from **Yallakora** 🏆⚽
- Comprehensive match metrics including:
  - Team names
  - Match scores
  - Match status
  - Match time
  - Round number
  - Championship name
- Robust error handling
- Clean CSV output format
- User-agent handling for reliable scraping

## 🚀 How to Use
1. **Set up your environment**:  
   Make sure you have Python installed on your system.

2. **Install dependencies**:  
   Run the following command to install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Scraper**:  
   Execute the script:
   ```bash
   python main.py
   ```
   The script will:
   - Prompt you to enter a date (MM/DD/YYYY format)
   - Fetch the latest football match data for that date from Yallakora
   - Process the information
   - Generate a CSV file (football_fixtures.csv)

4. **View the Results**:
   Open the generated `football_fixtures.csv` file in Excel:
   - Set the page layout from right to left to properly display the Arabic data
   - You may need to adjust column widths for optimal viewing

## 📊 Example Output

### CSV File (football_fixtures.csv)
| البطولة | رقم الجولة | موعد المباراة | الحالة | الفريق الثاني | نتيجة المباراة | الفريق الأول |
|---------|------------|---------------|--------|---------------|----------------|--------------|
| تصفيات أمم إفريقيا | الجولة الثالثة | 07:00:00 م | انتهت | اثيوبيا | 1 - 4 | غينيا |
| تصفيات أمم إفريقيا | الجولة الثالثة | 10:00:00 م | انتهت | أفريقيا الوسطى | 0 - 5 | المغرب |
| بطولة إفريقيا للأندية لكرة اليد | اليوم الثالث | 07:00:00 م | انتهت | أدجيدجا | 43 - 25 | آسفا |

Note: The table above is displayed from right to left to match the Arabic text direction.

## 💻 Code Highlights
### Error Handling
```python
def fetch_page_content(url):
    """Fetches the HTML content of a given URL."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }
    try:
        page = requests.get(url, headers=headers, timeout=5)
        page.raise_for_status()
        return page.content
    except requests.exceptions.HTTPError as http_error:
        print(f"HTTP error occurred: {http_error}")
    # ... more error handling
```

## 🛠️ Potential Enhancements
- Add command-line arguments for custom output file names
- Implement data comparison with historical records
- Add data visualization capabilities
- Create a simple web interface using Flask
- Add automated scheduling for regular data updates
- Implement data validation and cleaning
- Add support for different output formats (JSON, Excel)
- Include data visualization exports

## 👨‍💻 Author
Khaled Soudy

## 🧱 Project Structure
```
football-fixtures-scraper/
├── main.py          # Main script with scraping logic
├── requirements.txt # Project dependencies
├── .gitignore       # Git ignore file
└── README.md        # Project documentation
```

## 📦 Dependencies
The project relies on the following Python packages:
- beautifulsoup4==4.12.3
- certifi==2024.8.30
- charset-normalizer==3.4.0
- idna==3.10
- lxml==5.3.0
- requests==2.32.3
- soupsieve==2.6
- tabulate==0.9.0
- urllib3==2.2.3

## ⚠️ Disclaimer
Please ensure you follow Yallakora's robots.txt and terms of service when using this scraper. Be respectful of the website's resources and implement appropriate delays between requests if needed.

## 📞 Support
If you encounter any issues or have questions, please open an issue in the GitHub repository.

## 🤝 Contributing
Contributions are welcome! Feel free to submit pull requests or open issues to improve the project.

## 📄 License
This project is open source and available under the MIT License.

---
Stay updated with the latest football fixtures from Yallakora! ⚽📊