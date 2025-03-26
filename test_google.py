from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def test_google_search():
    # Point to the Selenium Grid Hub
    driver = webdriver.Remote(
        command_executor='http://selenium-grid-hub.selenium:4444/wd/hub',
        options=webdriver.ChromeOptions()
    )
    
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()

if __name__ == "__main__":
    test_google_search()
