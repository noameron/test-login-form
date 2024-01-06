import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def setup_driver_capabilities(request):
    options = webdriver.webdriver.AppiumOptions()
    options.set_capability('platformName', 'Android')
    options.set_capability('platformVersion', '11.0')
    options.set_capability('deviceName', 'emulator-5556')
    options.set_capability('appPackage', 'com.google.android.gm')
    options.set_capability('appActivity', '.ConversationListActivityGmail')
    options.set_capability('noReset', True)

    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', options=options)
    yield driver

    def teardown():
        driver.execute_script("mobile: shell", {
            "command": "am",
            "args": ["kill", "com.google.android.gm"]
        })
        driver.quit()

    request.addfinalizer(teardown)
    return driver

def test_appium_connection(setup_driver_capabilities):
    """
    Test case to check that Appium server is running and emulator is connected
    :param setup_driver_capabilities:
    :return:
    """
    driver = setup_driver_capabilities
    assert driver.session_id is not None, "Failed to create a session with emulator"


def test_gmail_app_opening(setup_driver_capabilities):
    """
    Test case to check that Gmail App is opened
    :param setup_driver_capabilities:
    :return:
    """
    driver = setup_driver_capabilities
    wait = WebDriverWait(driver, 20)

    elem_got_it_screen = wait.until(EC.visibility_of_element_located((By.ID, "com.google.android.gm:id/welcome_tour_got_it")))
    elem_got_it_screen.click()

    elem_setup_email = wait.until(EC.visibility_of_element_located((By.ID, "com.google.android.gm:id/setup_addresses_add_another")))
    elem_setup_email.click()

    elem_gmail = wait.until(EC.visibility_of_element_located((By.ID, "com.google.android.gm:id/account_setup_label")))
    elem_gmail.click()

    elem_gmail_login_page = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "android.widget.EditText")))
    assert elem_gmail_login_page is not None, "Failed to open Gmail App"


def test_bad_login_name_with_refresh(setup_driver_capabilities):
    """
    Test case to check that error message is displayed when user enters bad login name
    :param setup_driver_capabilities:
    :return:
    """
    driver = setup_driver_capabilities
    wait = WebDriverWait(driver, 20)
    expected_error_message = "Couldn’t find your Google Account"

    elem_got_it_screen = wait.until(
        EC.visibility_of_element_located((By.ID, "com.google.android.gm:id/welcome_tour_got_it")))
    elem_got_it_screen.click()

    elem_setup_email = wait.until(
        EC.visibility_of_element_located((By.ID, "com.google.android.gm:id/setup_addresses_add_another")))
    elem_setup_email.click()

    elem_gmail = wait.until(EC.visibility_of_element_located((By.ID, "com.google.android.gm:id/account_setup_label")))
    elem_gmail.click()

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "android.widget.EditText"))).send_keys("bad_email")

    driver.find_element(By.XPATH, "//android.widget.Button[@text='NEXT']").click()

    error_message_element = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                       "//android.view.View[@text='Couldn’t find your Google Account']")))
    error_message_text = error_message_element.text

    assert expected_error_message == error_message_text, "Bad email error message is not displayed"


def test_long_email_address(setup_driver_capabilities):
    """
    Test case to check that error message is displayed when user enters long email address
    :param setup_driver_capabilities:
    :return:
    """
    driver = setup_driver_capabilities
    wait = WebDriverWait(driver, 20)
    expected_error_message = "Enter a valid email or phone number"

    elem_got_it_screen = wait.until(
        EC.visibility_of_element_located((By.ID, "com.google.android.gm:id/welcome_tour_got_it")))
    elem_got_it_screen.click()

    elem_setup_email = wait.until(
        EC.visibility_of_element_located((By.ID, "com.google.android.gm:id/setup_addresses_add_another")))
    elem_setup_email.click()

    elem_gmail = wait.until(EC.visibility_of_element_located((By.ID, "com.google.android.gm:id/account_setup_label")))
    elem_gmail.click()

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "android.widget.EditText"))).send_keys("a" * 300)

    driver.find_element(By.XPATH, "//android.widget.Button[@text='NEXT']").click()

    error_message_element = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                       "//android.view.View[@text='Enter a valid email or phone number']")))
    error_message_text = error_message_element.text

    assert expected_error_message == error_message_text, "Invalid error message is not displayed"


def test_empty_email_address(setup_driver_capabilities):
    """
    Test case to check that error message is displayed when user enters empty email address
    :param setup_driver_capabilities:
    :return:
    """

    driver = setup_driver_capabilities
    wait = WebDriverWait(driver, 20)
    expected_error_message = "Enter an email or phone number"

    elem_got_it_screen = wait.until(
        EC.visibility_of_element_located((By.ID, "com.google.android.gm:id/welcome_tour_got_it")))
    elem_got_it_screen.click()

    elem_setup_email = wait.until(
        EC.visibility_of_element_located((By.ID, "com.google.android.gm:id/setup_addresses_add_another")))
    elem_setup_email.click()

    elem_gmail = wait.until(EC.visibility_of_element_located((By.ID, "com.google.android.gm:id/account_setup_label")))
    elem_gmail.click()

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "android.widget.EditText"))).send_keys("")

    driver.find_element(By.XPATH, "//android.widget.Button[@text='NEXT']").click()

    error_message_element = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                       "//android.view.View[@text='Enter an email or phone number']")))
    error_message_text = error_message_element.text

    assert expected_error_message == error_message_text, "Empty email error message is not displayed"


def test_special_characters_bad_email(setup_driver_capabilities):
    """
    Test case to check that error message is displayed when user enters special characters in email address
    :param setup_driver_capabilities:
    :return:
    """
    driver = setup_driver_capabilities
    wait = WebDriverWait(driver, 20)
    expected_error_message = "Enter a valid email or phone number"

    elem_got_it_screen = wait.until(
        EC.visibility_of_element_located((By.ID, "com.google.android.gm:id/welcome_tour_got_it")))
    elem_got_it_screen.click()

    elem_setup_email = wait.until(
        EC.visibility_of_element_located((By.ID, "com.google.android.gm:id/setup_addresses_add_another")))
    elem_setup_email.click()

    elem_gmail = wait.until(EC.visibility_of_element_located((By.ID, "com.google.android.gm:id/account_setup_label")))
    elem_gmail.click()

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "android.widget.EditText"))).send_keys("bad_email@#$%^&*()")

    driver.find_element(By.XPATH, "//android.widget.Button[@text='NEXT']").click()

    error_message_element = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                       "//android.view.View[@text='Enter a valid email or phone number']")))
    error_message_text = error_message_element.text

    assert expected_error_message == error_message_text, "Bad email error message is not displayed"
