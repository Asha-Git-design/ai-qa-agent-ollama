import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    # Setup: Initialize Chrome browser
    driver = webdriver.Chrome()
    yield driver
    # Teardown: Quit browser after test
    driver.quit()
