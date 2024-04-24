import os
import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Constants
SCRAPE_URL = "https://tensor.art/models"
HTML_FILENAME = "scraped.html"
WAIT_TIME = 5  # Adjust the waiting time as needed
while True:
    os.system("cls || clear")
    # Prompt user for selection
    TO_SCRAP = input("What do you want to scrap?\n1 - Models/Checkpoints\n2 - LORAs\n>>> ")
    
    # Process user input
    if TO_SCRAP == "1":
        TO_SCRAP = "LORA"
        JSON_FILENAME = "models_data.json"  # Update JSON filename for models/checkpoints
        break
    elif TO_SCRAP == "2":
        TO_SCRAP = "CHECKPOINT"
        JSON_FILENAME = "loras_data.json"  # Update JSON filename for LORAs
        break
    else:
        print("Invalid input. Please select only 1 or 2")
        time.sleep(3)



def save_webpage(url, filename, stype):
    """Save webpage source to a file."""
    # Create a new instance of the Chrome driver
    options = webdriver.ChromeOptions() # Create a ChromeOptions object
    options.add_argument("--enable-chrome-browser-cloud-management")
    options.add_argument("--log-level=3") # This sets the log level to suppress warnings


    driver = webdriver.Chrome(options=options)

    
    
    try:
        # Open the webpage
        driver.get(url)
        
        # Wait for user confirmation
        input("#"*50+"\nPress Enter when ready to save the webpage...\n")
        time.sleep(WAIT_TIME)  # Let the page load completely
        
        # Get the page source
        page_source = driver.page_source
        
        # Save the webpage content to a file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(page_source)
        
        print("Webpage saved successfully as", filename)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Close the browser
        driver.quit()

def parse_html_to_json(html_content):
    """Parse HTML content and extract relevant data to JSON."""
    soup = BeautifulSoup(html_content, 'html.parser')
    data = {}
    
    # Find all <a> tags
    for a_tag in soup.find_all('a', class_='group'):
        href = a_tag.get('href')
        model_id = href.split('/')[-1] if href else None
        
        h3_tag = a_tag.find('h3')
        model_name = h3_tag['title'].lstrip() if h3_tag else None
        
        if not model_id or not model_name:
            continue
        
        div_tag = a_tag.find_next('div', class_='flex-c absolute z-1 top-8 left-8 gap-4')
        if div_tag and TO_SCRAP in div_tag.text:#if lora or checkpoint detected
            continue  # Skip this iteration
        
        data[model_name] = f"https://tensor.art/models/{model_id}"
    
    return data

def update_json_data(data, json_file_path):
    """Update existing JSON file with new data."""
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            existing_data = json.load(json_file)
        existing_data.update(data)
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(existing_data, json_file, indent=4, ensure_ascii=False)
    else:
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

def main():
    # Step 1: Save webpage
    save_webpage(SCRAPE_URL, HTML_FILENAME, TO_SCRAP)
    
    # Step 2: Read HTML content from the file
    with open(HTML_FILENAME, "r", encoding="utf-8") as html_file:
        html_content = html_file.read()
    
    # Step 3: Parse HTML content and extract data
    data = parse_html_to_json(html_content)
    
    # Step 4: Update JSON file with new data
    update_json_data(data, JSON_FILENAME)
    
    # Step 5: Print the updated dictionary
    os.system("cls || clear")
    print(data)
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
