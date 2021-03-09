import pytest
from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import random


scenarios('../features/items_cart.feature')


@then('I click on random items that needs to be added')
def addItems(browser):
    randomNumber = random.randint(1, 6)
    navigate = browser.find_element_by_xpath((
        '//*[@id=\"inventory_container\"]/div/div[{0}]/div[3]/button').format(
        randomNumber))
    navigate.click()


@then('I move to cart page')
def cart(browser):
    browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div[3]/a").click()


@then('I click on checkout button')
def checkout(browser):
    browser.find_element_by_link_text('CHECKOUT').click()


@then('I remove items in the cart page')
def remove(browser):
    browser.find_element_by_xpath(
        '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/button').click()


@then('I click on random items that needs to be added and click remove')
def add_remove(browser):
    navigate = browser.find_element_by_xpath((
        '//*[@id=\"inventory_container\"]/div/div[{0}]/div[3]/button').format(
        randomNumber))
    navigate.click()
    navigate.click()