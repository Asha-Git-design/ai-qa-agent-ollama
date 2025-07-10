import pytest
from selenium import webdriver
import allure

@allure.epic("Authentication Module")
@allure.feature("Login")
@allure.story("Valid User Login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke", "ui", "chrome")
@allure.title("Test Valid Login with Screenshot")
def test_login():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        assert "Practice Test Automation" in driver.title

        driver.find_element("name", "username").send_keys("student")
        driver.find_element("name", "password").send_keys("Password123")
        driver.find_element("id", "submit").click()

        assert "Logged In Successfully" in driver.page_source

    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(),
                      name="Failure Screenshot",
                      attachment_type=allure.attachment_type.PNG)
        raise e

    finally:
        driver.quit()