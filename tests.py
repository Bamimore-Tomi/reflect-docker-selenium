from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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

driver.get('https://www.google.com/')
response_start = driver.execute_script("return window.performance.timing.responseStart")
dom_complete = driver.execute_script("return window.performance.timing.domComplete")
 
load_time = dom_complete - response_start
 
print("Load time", load_time)
driver.quit()