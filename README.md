# Tensor.Art Scraper

This Python script automates the process of scraping model-related data (such as Models/Checkpoints, LORAs, DORAs, LOCONs, LYCORIS, or EMBEDDINGs) from [Tensor.art](https://tensor.art/), extracting relevant information, and storing it in a JSON file.

## Description

The script performs the following tasks:

1. **User Input for Data Type**: Prompts the user to select the type of data they want to scrape (e.g., Models/Checkpoints, LORAs, etc.).
2. **Launches Chrome Browser**: Uses Selenium WebDriver to launch a Chrome browser.
3. **Navigates to Tensor.Art Models Page**: Directs the browser to the [Tensor.art models](https://tensor.art/models) webpage.
4. **User Confirmation**: Waits for the user to confirm when the page is ready to be scraped.
5. **Saves Webpage Source**: Captures and saves the webpage's HTML content.
6. **Parses HTML Content**: Utilizes BeautifulSoup to parse the HTML and extract relevant model data.
7. **Filters Data**: Filters the scraped data based on user selection (e.g., SDXL models, LORAs, etc.).
8. **Stores Data in JSON**: Saves the extracted data into a JSON file. The filename is determined by the user's choice (e.g., `models_data.json` for Models/Checkpoints, `loras_data.json` for LORAs).
9. **Updates Existing JSON**: If the JSON file already exists, it updates it with new data while preserving existing information.
10. **Displays Extracted Data**: The script will print the extracted data to the console and remove the temporary HTML file.

## Installation

1. **Python 3.x**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).
2. **Install Required Packages**: Use pip to install the required Python packages:
   ```bash
   pip install selenium beautifulsoup4
   ```
3. **Download Chrome WebDriver**: Download the appropriate [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for your version of Chrome. Ensure it's accessible via your system's PATH.

## Usage

1. **Clone or Download the Script**: Clone this repository or download the script to your local machine.
2. **Run the Script**: Navigate to the directory containing the script using a terminal or command prompt, and execute:
   ```bash
   python TensorScraper.py
   ```
3. **Follow the On-Screen Instructions**: Select the type of data you want to scrape and follow the prompts.
4. **View the Results**: The scraped data will be stored in a JSON file named according to the data type you selected (e.g., `models_data.json` for Models/Checkpoints). The JSON file will contain the data categorized by SD, SDXL, SD3, Kolors, and HunyuanDiT.

## Customization

You can customize the script by modifying the constants at the beginning of the script, such as `SCRAPE_URL`, `HTML_FILENAME`, `JSON_FILENAME`, and `WAIT_TIME`.

## Requirements

- Python 3.x
- Selenium WebDriver
- Chrome browser
- Chrome WebDriver
- BeautifulSoup

## Contributing

Pull requests are welcome! If you want to make significant changes, please open an issue first to discuss what you would like to modify.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE](LICENSE) file for details.

---
