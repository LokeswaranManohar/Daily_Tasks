import pytest
from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

scenarios('../features/new.feature')


# @when('I type the username "<username>" and password "<password>"')
# def search_user(browser, username, password):
#     browser.find_element_by_name('user-name').send_keys(username)
#     browser.find_element_by_name('password').send_keys(password)
#
#
# @when('I click on login button')
# def login(browser):
#     browser.find_element_by_id('login-button').click()


@then('Validate the result page with Page Title')
def result(browser):
    # WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located(By.ID, 'item_4_img_link'))
    expectedUrl = 'https://www.saucedemo.com/inventory.html'
    actualUrl = browser.current_url
    assert actualUrl == expectedUrl


@then('Validate the error message')
def error(browser):
    message = browser.find_element_by_xpath('//*[@id="login_button_container"]/div/form/h3')
    assert message.text == "Epic sadface: Sorry, this user has been locked out."
