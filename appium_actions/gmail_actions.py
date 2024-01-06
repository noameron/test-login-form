from appium.webdriver import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def gmail_login_screen_actions(driver: webdriver, timeout: int = 20):
    """
    Perform actions on Gmail login screen
    :param driver: Appium driver
    :param timeout: Timeout in seconds
    """
    wait = WebDriverWait(driver, timeout)
    elem_got_it_screen = wait.until(
        EC.visibility_of_element_located((By.ID, "com.google.android.gm:id/welcome_tour_got_it")))
    elem_got_it_screen.click()

    elem_setup_email = wait.until(
        EC.visibility_of_element_located((By.ID, "com.google.android.gm:id/setup_addresses_add_another")))
    elem_setup_email.click()

    elem_gmail = wait.until(EC.visibility_of_element_located((By.ID, "com.google.android.gm:id/account_setup_label")))
    elem_gmail.click()


def click_next(driver: webdriver):
    """
    Click on Next button
    :param driver:
    :return:
    """
    driver.find_element(By.XPATH, "//android.widget.Button[@text='NEXT']").click()


def fill_email_address_box(driver: webdriver, text_to_fill: str, timeout: int = 20):
    """
    Fill email address box with text_to_fill
    :param driver:
    :param text_to_fill:
    :param timeout:
    :return:
    """
    wait = WebDriverWait(driver, timeout)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "android.widget.EditText"))).send_keys(text_to_fill)


def fill_password_box(driver: webdriver, text_to_fill: str, timeout: int = 20):
    """
    Fill password address box with text_to_fill
    :param driver:
    :param text_to_fill:
    :param timeout:
    :return:
    """
    wait = WebDriverWait(driver, timeout)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "android.widget.EditText"))).send_keys(text_to_fill)
