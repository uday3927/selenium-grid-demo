from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_google_search():
    # Setup Remote WebDriver using Selenium Grid
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor='http://10.105.167.44:4444/wd/hub',
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
        time.sleep(2)
        
        # Assert search results page is loaded
        assert "Testkube Selenium Grid" in driver.title
        
        print("Google search test completed successfully!")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    test_google_search()
