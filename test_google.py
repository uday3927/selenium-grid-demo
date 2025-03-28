import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google_search():
    # Get Hub URL from environment variable
    hub_url = os.getenv('SELENIUM_HUB_URL', 'http://10.105.167.44:4444/wd/hub')
    
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor=hub_url,
        options=options
    )
    
    try:
        # Navigate to Google
        driver.get("https://www.google.com")
        
        # Find search box and perform search
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Testkube Selenium Grid")
        search_box.send_keys(Keys.RETURN)
        
        # Explicit wait for title update
        WebDriverWait(driver, 10).until(
            EC.title_contains("Testkube Selenium Grid")
        )
        
        # Assertion with descriptive error
        assert "Testkube Selenium Grid" in driver.title, \
            f"Expected 'Testkube Selenium Grid' in title, got '{driver.title}'"
            
    finally:
        # Critical cleanup - always executes
        driver.quit()
