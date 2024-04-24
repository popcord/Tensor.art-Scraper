
---

# Web Scraping and JSON Data Extraction

This Python script automates the process of scraping models and/or LORAs from [Tensor.art](https://tensor.art/), extracting relevant data, and storing it in a JSON file.

## Description

The script performs the following tasks:

1. Launches a Chrome browser using Selenium WebDriver.
2. Navigates to the [Tensor.art models](https://tensor.art/models) webpage URL.
3. Waits for user confirmation before proceeding to save the webpage source.
4. Parses the HTML content using BeautifulSoup to extract data.
5. Filters out unwanted data based on specified conditions(non-ascii characters).
6. Stores the extracted data in a JSON file.
7. Updates an existing JSON file with new data, if available.
8. Displays the extracted data on the console.

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install the required Python packages using pip:
   ```
   pip install selenium beautifulsoup4
   ```
3. Download the appropriate [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for your Chrome browser version and ensure it's in your system PATH.

## Usage

1. Clone or download the script to your local machine.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using the following command:
   ```
   python TensorScraper.py
   ```
4. Follow the on-screen instructions to proceed with the web scraping process.
5. Once completed, the extracted data will be stored in a JSON file named `models_data.json` or `loras_data.json`, depending on the user's choice.
6. You can customize the script by modifying the constants defined in the script, such as `SCRAPE_URL`, `HTML_FILENAME`, `JSON_FILENAME`, and `WAIT_TIME`.

## Requirements

- Python 3.x
- Selenium WebDriver
- Chrome browser
- Chrome WebDriver
- BeautifulSoup

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE](LICENSE) file for details.

---
