from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Define options for running the chromedriver
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_prefs = {}
chrome_options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}

# Initialize a new chrome driver instance
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.saucedemo.com/')
username = driver.find_element(By.ID,"user-name")
password = driver.find_element(By.ID,"password")
login_button = driver.find_element(By.ID,"login-button")
username.send_keys("standard_user")
username.send_keys("secret_sauce")
login_button.click()
print(driver.current_url())
assert driver.current_url()=="https://www.saucedemo.com/inventory.html"
driver.quit()