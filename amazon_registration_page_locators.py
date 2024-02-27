from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# By CSS
driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')
# By TAG + Class
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')
# CSS connect by ID
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
driver.find_element(By.CSS_SELECTOR, '#ap_email')
# By attr
driver.find_element(By.CSS_SELECTOR, "[placeholder='At least 6 characters']")
# From parent => child
driver.find_element(By.CSS_SELECTOR,"#ap_password [class*='a-alert-content']")
# By ID
driver.find_element(By.ID, '#ap_password_check')
driver.find_element(By.ID, '#continue')
# By attr
driver.find_element(By.CSS_SELECTOR, "[href*='condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "[href*='notification_privacy_notice']")
driver.find_element(By.CSS_SELECTOR, "[href*='page']")
