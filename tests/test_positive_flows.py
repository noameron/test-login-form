import pytest
from appium.webdriver import webdriver
from selenium.webdriver.common.by import By

from appium_actions.gmail_actions import click_next, gmail_login_screen_actions, fill_email_address_box
from main import setup_driver_capabilities


@pytest.mark.usefixtures("setup_driver_capabilities")
class TestPositiveFlows:
    """
    Test class to test positive flows on Gmail login form
    """
    valid_email_address = "noameron3"

    @staticmethod
    def verify_appium_connection(driver: webdriver):
        """
        Test case to check that Appium server is running and emulator is connected
        :param driver: Appium driver
        :return:
        """
        assert driver.session_id is not None, "Failed to create a session with emulator"

    def test_valid_email_address_without_domain(self, setup_driver_capabilities):
        """
        Verifies a valid email address without domain
        :param setup_driver_capabilities:
        :return:
        """
        driver = setup_driver_capabilities
        gmail_login_screen_actions(driver)

        fill_email_address_box(driver, self.valid_email_address)
        click_next(driver)

        welcome_element = driver.find_element(By.XPATH, "//android.view.View[@resource-id='headingText']")

        assert welcome_element.text is not None, "Failed to login with valid email address"

    def test_valid_email_address_with_domain(self, setup_driver_capabilities):
        """
        Verifies a valid email address without domain
        :param setup_driver_capabilities:
        :return:
        """
        driver = setup_driver_capabilities
        gmail_login_screen_actions(driver)

        fill_email_address_box(driver, self.valid_email_address + "@gmail.com")
        click_next(driver)

        welcome_element = driver.find_element(By.XPATH, "//android.view.View[@resource-id='headingText']")

        assert welcome_element.text is not None, "Failed to login with valid email address"


