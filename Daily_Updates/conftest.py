import pytest
from selenium import webdriver
from pytest_bdd import given, when


SwagLabs_Home = 'https://www.saucedemo.com/'


@pytest.fixture
def browser():
    browse = webdriver.Chrome()
    browse.implicitly_wait(10)
    yield browse
    browse.quit()


@given('the SwagLabs home page is displayed')
def swag_home(browser):
    browser.get(SwagLabs_Home)
    browser.maximize_window()


@when('the user type "<username>"')
def search_user(browser, username):
    browser.find_element_by_name('user-name').send_keys(username)
    time.sleep(2)


@when('the user type "<password>"')
def search_pas(browser, password):
    browser.find_element_by_name('password').send_keys(password)
    


@when('the user click login')
def login(browser):
    browser.find_element_by_id('login-button').click()


@when('I type the username "<username>" and password "<password>"')
def search_user(browser, username, password):
    browser.find_element_by_name('user-name').send_keys(username)
    browser.find_element_by_name('password').send_keys(password)


@when('I click on login button')
def login(browser):
    browser.find_element_by_id('login-button').click()


@when('The result page is displayed')
def result(browser):
    # WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located(By.ID, 'item_4_img_link'))
    expectedUrl = 'https://www.saucedemo.com/inventory.html'
    actualUrl = browser.current_url
    assert actualUrl == expectedUrl

