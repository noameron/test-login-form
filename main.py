from telnetlib import EC

import pytest
from appium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def setup_driver_capabilities():
    options = webdriver.webdriver.AppiumOptions()
    options.set_capability('platformName', 'Android')
    options.set_capability('platformVersion', '10.0')
    options.set_capability('deviceName', 'emulator-5554')
    options.set_capability('appPackage', 'com.google.android.gm')
    options.set_capability('appActivity', '.ConversationListActivityGmail')
    options.set_capability('noReset', True)

    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', options=options)
    yield driver
    driver.quit()


def test_appium_connection(setup_driver_capabilities):
    driver = setup_driver_capabilities
    assert driver.session_id is not None, "Failed to create a session with emulator"


def test_chrome_opening(setup_driver_capabilities):
    driver = setup_driver_capabilities
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "com.google.android.gm:id/welcome_tour_got_it").click()
    driver.find_element(By.ID, "com.google.android.gm:id/setup_addresses_add_another").click()
    driver.find_element(By.ID, "com.google.android.gm:id/account_setup_label").click()



def test_bad_login_name(setup_driver_capabilities):
    driver = setup_driver_capabilities
    des_url = "https://accounts.google.com/v3/signin/identifier?flowEntry=ServiceLogin&flowName=GlifWebSignIn&hl=en-GB&ifkv=ASKXGp3kf4lIcrKOceS6o4MUCwgsrezbEK-iwAIescnJGT3D9NoW36GABrJRhfHHiiPRRQyUdipi0Q&dsh=S1913610772%3A1704452149621372&theme=glif"
    driver.get(des_url)

    driver.find_element(By.ID, "identifierId").send_keys("bad_email")
    driver.find_element(By.ID, "identifierNext").click()
    driver.implicitly_wait(5)
    try:
        is_bad_email_error = driver.find_element(By.CLASS_NAME, "jibhHc").is_displayed()
    except NoSuchElementException:
        is_bad_email_error = False

    assert is_bad_email_error, "Bad email error is not displayed"

def test_bad_login_name_with_refresh(setup_driver_capabilities):
    driver = setup_driver_capabilities
    des_url = "https://accounts.google.com/v3/signin/identifier?flowEntry=ServiceLogin&flowName=GlifWebSignIn&hl=en-GB&ifkv=ASKXGp3kf4lIcrKOceS6o4MUCwgsrezbEK-iwAIescnJGT3D9NoW36GABrJRhfHHiiPRRQyUdipi0Q&dsh=S1913610772%3A1704452149621372&theme=glif"
    driver.get(des_url)

    driver.find_element(By.ID, "identifierId").send_keys("bad_email")
    driver.find_element(By.ID, "identifierNext").click()
    driver.implicitly_wait(5)
    try:
        is_bad_email_error = driver.find_element(By.CLASS_NAME, "jibhHc").is_displayed()
    except NoSuchElementException:
        is_bad_email_error = False

    assert is_bad_email_error, "Bad email error is not displayed"

    driver.refresh()
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "identifierId").send_keys("bad_email")
    driver.find_element(By.ID, "identifierNext").click()
    try:
        is_bad_email_error = driver.find_element(By.CLASS_NAME, "jibhHc").is_displayed()
    except NoSuchElementException:
        is_bad_email_error = False

    assert is_bad_email_error, "Bad email error is not displayed"