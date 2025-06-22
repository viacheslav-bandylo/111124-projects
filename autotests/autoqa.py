import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(params=["Edge"])
def driver(request):
    driver = webdriver.Edge()
    yield driver
    driver.quit()

# creating some auto qa
def test_hello_user(driver):
    driver.get("http://127.0.0.1:8000/app/hello")
    hello_user = driver.find_element(By.CSS_SELECTOR, "body > h1")
    assert hello_user.text == "Hello, großpapa!"