import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_google_search():
    # Get Hub URL from environment variable
    hub_url = os.getenv('SELENIUM_HUB_URL', 'http://10.105.167.44:4444/wd/hub')  # Falls back to your current URL
    
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor=hub_url,  # Now uses the environment variable
        options=options
    )
    
    try:
        # Navigate to Google
        driver.get("https://www.google.com")
        
        # Find search box and perform search
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Testkube Selenium Grid")
        search_box.send_keys(Keys.RETURN)
        
        # Wait for results
        driver.implicitly_wait(10)
        
        # Assert search results page is loaded
        assert "Testkube Selenium Grid" in driver.title, "Search results page not loaded correctly"
        
    finally:
        driver.quit()
