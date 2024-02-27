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

# css, connect by ID
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
# By class
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag-us')
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag-us.icp-nav-flag')
# By TAG + class / id/ attr
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag-us.icp-nav-flag')
# By attr
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")
# Partial attr:
driver.find_element(By.CSS_SELECTOR, "[aria-describedby*='Dropdown']")
driver.find_element(By.CSS_SELECTOR, "[class*='nav-search-dropdown'] [[aria-describedby*='Dropdown']")

# From parent => child
driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='condition']")
