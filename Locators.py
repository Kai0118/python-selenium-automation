#Locators

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
#
# # get the path to the ChromeDriver executable
# driver_path = ChromeDriverManager().install()
#
# # create a new Chrome browser instance
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()
#
# driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
# sleep(5)
#
#
# #
# # Amazon logo
# driver.find_element(By.XPATH,"//i[@aria-label='Amazon']")
#
# # Amazon email field
# driver.find_element(By.ID,'ap_email')
#
# # Amazon continue button
# driver.find_element(By.ID,'continue')
#
# # Amazon Conditions of use link
# driver.find_element(By.XPATH,"//a[@target='_blank']")
#
# # Amazon Privacy Notice link
# driver.find_element(By.XPATH,"//a[@rel='noopener']")
#
# # # Amazon Need help link
# driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']")
#
# # Amazon Forgot your password link
# driver.find_element(By.ID,'auth-fpp-link-bottom')
#
# # Amazon Other issues with Sign-In link
# driver.find_element(By.ID,'ap-other-signin-issues-link')
#
# # Create your Amazon account button
# driver.find_element(By.ID,'createAccountSubmit')
#
#
# print('Test Passed')
#
# driver.quit()

# Target Test Case

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

# 1. Open https://www.target.com/
driver.get('https://www.target.com/')
#
# 2. Click SignIn button
driver.find_element(By.XPATH, "//a[@aria-label='Account, sign in']").click()

# 3. Click SignIn from side navigation
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
# #
# # 4. Verify SignIn page opened:
# # “Sign in to your Target account” text is shown,
# # SignIn button is shown
sleep(3)
driver.find_element(By.XPATH,"//h1[@class='styles__StyledHeading-sc-1xmf98v-0 styles__AuthHeading-sc-kz6dq2-2 jhKFiw kcHdEa']")
driver.find_element(By.ID, 'login')


print('Test Passed')

driver.quit()