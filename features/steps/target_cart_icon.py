# Target BDD Test Case

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# @given('Open Target main page')
# def open_target_main_page(context):
#     context.driver.get('https://www.target.com/')


@when('Clicking on the cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()
    sleep(6)


@then('"Your cart is empty" message is shown')
def verify_empty_cart_message(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[@class='styles__StyledHeading-sc-1xmf98v-0 lfA-Dem']").text
    assert 'Your cart is empty' in actual_text, f'Expected word not in {actual_text}'
    print('Test case passed')