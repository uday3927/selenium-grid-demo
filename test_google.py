import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_google_search():
    # Verify Grid connection
    hub_url = os.getenv('SELENIUM_HUB_URL', 'http://selenium-hub.selenium:4444/wd/hub')  # Use service DNS
    print(f"\n=== Connecting to Selenium Hub at: {hub_url} ===")
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # Recommended for containerized tests
    driver = webdriver.Remote(
        command_executor=hub_url,
        options=options
    )
    
    try:
        # Step 1: Load Google
        print("Navigating to Google...")
        driver.get("https://www.google.com")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        
        # Step 2: Perform search
        search_term = "Testkube Selenium Grid"
        print(f"Searching for: {search_term}")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)
        
        # Step 3: Wait for results - multiple verification points
        try:
            # Option 1: Wait for search results container
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "search"))
            )
            
            # Option 2: Verify title pattern
            WebDriverWait(driver, 5).until(
                lambda d: d.title.startswith(search_term)
            )
            
            print(f"SUCCESS! Final title: {driver.title}")
            
        except TimeoutException:
            # Debugging info
            print(f"\n=== DEBUG INFO ===")
            print(f"Current URL: {driver.current_url}")
            print(f"Page title: {driver.title}")
            print(f"Page source length: {len(driver.page_source)} chars")
            driver.save_screenshot("debug.png")
            raise
            
    finally:
        driver.quit()
