import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google_search():
    hub_url = os.getenv('SELENIUM_HUB_URL', 'http://10.105.167.44:4444/wd/hub')
    
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor=hub_url,
        options=options
    )
    
    try:
        # Debug connection
        print(f"Connecting to Selenium Hub at: {hub_url}")
        
        # Navigate to Google with explicit wait for page load
        driver.get("https://www.google.com")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        
        # Perform search with debugging
        search_box = driver.find_element(By.NAME, "q")
        search_term = "Testkube Selenium Grid"
        print(f"Entering search term: {search_term}")
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)
        
        # Wait for results - more flexible condition
        WebDriverWait(driver, 15).until(
            lambda d: search_term.lower() in d.title.lower()
        )
        print(f"Final page title: {driver.title}")
        
    except Exception as e:
        # Capture page source if test fails
        with open("page_source.html", "w") as f:
            f.write(driver.page_source)
        raise
    finally:
        driver.quit()
