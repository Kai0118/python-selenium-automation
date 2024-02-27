from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')


@when('Click Sign in')
def click_on_sign_in_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '[href="/account?prehydrateClick=true"][aria-label="Account, sign in"]').click()
    sleep(6)


@when('From right side navigation menu, click Sign In')
def click_on_sign_in_on_side_navigation_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href='/account'][data-test='accountNav-signIn']").click()


@then('verify Sign In form opened')
def verify_sign_in_form_is_opened(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[method='post']").text
    assert 'Sign in with password' in actual_text, f'Expected word not in {actual_text}'
    print('Test case passed')