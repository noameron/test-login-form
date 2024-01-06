import pytest
from appium.webdriver import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from main import setup_driver_capabilities
from appium_actions.gmail_actions import click_next, gmail_login_screen_actions, fill_email_address_box, fill_password_box
from tests.gmail_app_enums import GmailCreds, ErrorMessages


@pytest.mark.usefixtures("setup_driver_capabilities")
class TestNegativeFlows:
    """
    Test class to test negative flows on Gmail login form
    """

    @staticmethod
    def verify_appium_connection(driver):
        """
        Test case to check that Appium server is running and emulator is connected
        :param driver: Appium driver
        :return:
        """
        assert driver.session_id is not None, "Failed to create a session with emulator"

    @staticmethod
    def validate_error_message(driver: webdriver, expected_error_message):
        """
        Validate that the error message matches the expected message
        :param driver: Appium driver
        :param expected_error_message: Expected error message
        """
        wait = WebDriverWait(driver, 20)
        error_message_element = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                           f"//android.view.View[@text='{expected_error_message}']")))
        error_message_text = error_message_element.text
        assert expected_error_message == error_message_text, f"Error message mismatch: {error_message_text}"

    def test_bad_login_name_with_refresh(self, setup_driver_capabilities):
        """
        Test case to check that error message is displayed when user enters bad login name
        :param setup_driver_capabilities:
        :return:
        """
        driver = setup_driver_capabilities
        self.verify_appium_connection(driver)
        expected_error_message = ErrorMessages.BAD_EMAIL_ADDRESS.value

        gmail_login_screen_actions(driver)

        fill_email_address_box(driver, GmailCreds.BAD_EMAIL_ADDRESS.value)

        click_next(driver)

        self.validate_error_message(driver, expected_error_message)

    def test_long_email_address(self, setup_driver_capabilities):
        """
        Test case to check that error message is displayed when user enters long email address
        :param setup_driver_capabilities:
        :return:
        """
        driver = setup_driver_capabilities
        self.verify_appium_connection(driver)
        expected_error_message = ErrorMessages.NOT_VALID_EMAIL_ADDRESS.value

        gmail_login_screen_actions(driver)

        fill_email_address_box(driver, "a" * 300)

        click_next(driver)

        self.validate_error_message(driver, expected_error_message)

    def test_empty_email_address(self, setup_driver_capabilities):
        """
        Test case to check that error message is displayed when user enters empty email address
        :param setup_driver_capabilities:
        :return:
        """

        driver = setup_driver_capabilities
        self.verify_appium_connection(driver)
        expected_error_message = ErrorMessages.NOT_VALID_EMAIL_ADDRESS.value

        gmail_login_screen_actions(driver)

        fill_email_address_box(driver, "")

        click_next(driver)

        self.validate_error_message(driver, expected_error_message)

    def test_special_characters_bad_email(self, setup_driver_capabilities):
        """
        Test case to check that error message is displayed when user enters special characters in email address
        :param setup_driver_capabilities:
        :return:
        """
        driver = setup_driver_capabilities
        self.verify_appium_connection(driver)
        expected_error_message = ErrorMessages.NOT_VALID_EMAIL_ADDRESS.value

        gmail_login_screen_actions(driver)

        fill_email_address_box(driver, GmailCreds.BAD_EMAIL_ADDRESS_SPECIAL_CHARS.value)

        click_next(driver)

        self.validate_error_message(driver, expected_error_message)

    def test_bad_domain(self, setup_driver_capabilities):
        """
        Test case to check that error message is displayed when user enters bad domain in email address
        :param setup_driver_capabilities:
        :return:
        """
        driver = setup_driver_capabilities
        self.verify_appium_connection(driver)
        expected_error_message = ErrorMessages.BAD_EMAIL_ADDRESS.value

        gmail_login_screen_actions(driver)

        fill_email_address_box(driver, GmailCreds.EMAIL_ADDRESS_WRONG_DOMAIN.value)

        click_next(driver)

        self.validate_error_message(driver, expected_error_message)

    def test_no_password(self, setup_driver_capabilities):
        """
        Test case to check that error message is displayed when user enters no password
        :param setup_driver_capabilities:
        :return:
        """
        driver = setup_driver_capabilities
        self.verify_appium_connection(driver)
        wait = WebDriverWait(driver, 20)
        expected_error_message = ErrorMessages.NO_PASSWORD.value

        gmail_login_screen_actions(driver)

        fill_email_address_box(driver, GmailCreds.EMAIL_ADDRESS.value)

        click_next(driver)

        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//android.view.View[@resource-id='headingText']")))

        fill_password_box(driver, "")

        click_next(driver)
        self.validate_error_message(driver, expected_error_message)

    def test_bad_password(self, setup_driver_capabilities):
        """
        Test case to check that error message is displayed when user enters no password
        :param setup_driver_capabilities:
        :return:
        """
        driver = setup_driver_capabilities
        self.verify_appium_connection(driver)
        wait = WebDriverWait(driver, 20)
        expected_error_message = ErrorMessages.BAD_PASSWORD.value

        gmail_login_screen_actions(driver)

        fill_email_address_box(driver, GmailCreds.EMAIL_ADDRESS.value)

        click_next(driver)

        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//android.view.View[@resource-id='headingText']")))

        fill_password_box(driver, GmailCreds.BAD_PASSWORD.value)

        click_next(driver)
        self.validate_error_message(driver, expected_error_message)


