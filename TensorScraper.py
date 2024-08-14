import os, json, time, re
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
    TO_SCRAP = input("What do you want to scrap?\n1 - Models/Checkpoints\n2 - LORAs\n3 - DORAs\n4 - LOCONs\n5 - LYCORYS\n6 - EMBEDDING\n>>> ")
    
    # Process user input
    if TO_SCRAP == "1":
        TO_SCRAP = "CHECKPOINT"
        JSON_FILENAME = "models_data.json"  # Update JSON filename for models/checkpoints
        break
    elif TO_SCRAP == "2":
        TO_SCRAP = "LORA"
        JSON_FILENAME = "loras_data.json"  # Update JSON filename for LORAs
        break
    elif TO_SCRAP == "3":
        TO_SCRAP = "DORA"
        JSON_FILENAME = "doras_data.json"  # Update JSON filename for DORAs
        break      
    elif TO_SCRAP == "4":
        TO_SCRAP = "LOCON"
        JSON_FILENAME = "locons_data.json"  # Update JSON filename for LOCONs
        break  
    elif TO_SCRAP == "5":
        TO_SCRAP = "LYCORIS"
        JSON_FILENAME = "lycoris_data.json"  # Update JSON filename for LYCORIS
        break
    elif TO_SCRAP == "6":
        TO_SCRAP = "EMBEDDING"
        JSON_FILENAME = "embedding_data.json"  # Update JSON filename for EMBEDDING
        break  
    else:
        print("Invalid input. Please select only between 1-6")
        time.sleep(3)

        
# How to use
print("How to use: To find what you're looking for, simply scroll until you find something that suits your needs. For more precise results, you can also use research tools, tags, and filters available on the website.\n"+"="*10)



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
        input("#"*50+"\nPress Enter when you are ready to save the webpage...\n")
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
    
    if os.path.exists(JSON_FILENAME):
        with open(JSON_FILENAME, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    else:
        data = {'SD': {}, 'SDXL': {}, 'SD3': {}, 'Kolors': {}, 'HunyuanDiT': {}} 
    
    # Find all <a> tags
    for a_tag in soup.find_all('a', class_='group'):
        href = a_tag.get('href')
        model_id = href.split('/')[-2] if href else None
        if model_id is not None and not model_id.isdigit():
            model_id = href.split('/')[-1] if href else None
        
        h3_tag = a_tag.find('h3')
        if h3_tag:
            model_name = re.sub(r'[^a-zA-Z0-9-]', '', h3_tag['title'].lstrip())  # Remove all characters except letters, numbers, and "-"
        else:
            model_name = None
        
        if not model_id or not model_name:
            continue
        
        div_tag = a_tag.find_next('div', class_='flex-c absolute z-1 top-8 left-8 gap-4')
        if div_tag and not TO_SCRAP in div_tag.text:  # if lora or checkpoint detected
            continue  # Skip this iteration

        if div_tag and " XL " in div_tag.text:
            if model_name not in data['SDXL']:
                data['SDXL'][model_name] = f"{model_id}"
        elif div_tag and " SD3 " in div_tag.text:
            if model_name not in data['SD3']:
                data['SD3'][model_name] = f"{model_id}"
        elif div_tag and " Kolors " in div_tag.text:
            if model_name not in data['Kolors']:
                data['SD3'][model_name] = f"{model_id}"
        elif div_tag and " HunyuanDiT " in div_tag.text:
            if model_name not in data['HunyuanDiT']:
                data['SD3'][model_name] = f"{model_id}"
        else:
            if model_name not in data['SD']:
                data['SD'][model_name] = f"{model_id}"

    
    return data


def update_json_data(data, json_file_path):
    """Update existing JSON file with new data."""
    if os.path.exists(json_file_path):
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
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
    if os.path.exists(HTML_FILENAME):
        os.remove(HTML_FILENAME)
    input("Press Enter to exit...")
    

if __name__ == "__main__":
    main()
