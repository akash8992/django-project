from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

# Path to your WebDriver (replace with the actual path to your chromedriver)
CHROME_DRIVER_PATH = 'C:/WebDrivers/chromedriver.exe'

def scrape_business_details(url):
    # Set up the Selenium WebDriver
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    
    try:
        # Open the URL
        driver.get(url)
        
        # Wait for the page to load (adjust time as needed for your internet speed or the website's response time)
        time.sleep(5)
        
        # Extract the page source after JavaScript has loaded
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Find all business containers (adjust class names based on the website's structure)
        business_list = soup.find_all('div', class_='ypresult')  # Update the 'ypresult' class if necessary
        businesses = []
        
        for business in business_list:
            try:
                # Extract business name
                name_tag = business.find('a', class_='ypname')  # Update 'ypname' class if necessary
                name = name_tag.get_text(strip=True) if name_tag else "N/A"
                
                # Extract address
                address_tag = business.find('div', class_='ypaddress')  # Update 'ypaddress' class if necessary
                address = address_tag.get_text(strip=True) if address_tag else "N/A"
                
                # Extract phone number
                phone_tag = business.find('div', class_='contact')  # Update 'contact' class if necessary
                phone = phone_tag.get_text(strip=True) if phone_tag else "N/A"
                
                # Extract pin code from the address
                pin_code = address.split()[-1] if address != "N/A" else "N/A"
                
                # Append details to the list
                businesses.append({
                    'Name': name,
                    'Address': address,
                    'Phone': phone,
                    'Pin Code': pin_code
                })
            except Exception as e:
                print(f"Error parsing a business: {e}")
        
        return businesses
    finally:
        # Close the browser
        driver.quit()

# URL to scrape
url = "http://yellowpages.in/hyderabad/food-and-beverages/606286653"  # Ensure this is the correct URL

# Call the function and print results
businesses = scrape_business_details(url)
for index, business in enumerate(businesses, 1):
    print(f"Business {index}:")
    print(f"Name: {business['Name']}")
    print(f"Address: {business['Address']}")
    print(f"Phone: {business['Phone']}")
    print(f"Pin Code: {business['Pin Code']}")
    print("-" * 30)
