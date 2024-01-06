from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def gmail_login_screen_actions(driver):
    """
    Perform actions on Gmail login screen
    :param driver: Appium driver
    """
    wait = WebDriverWait(driver, 20)
    elem_got_it_screen = wait.until(
        EC.visibility_of_element_located((By.ID, "com.google.android.gm:id/welcome_tour_got_it")))
    elem_got_it_screen.click()

    elem_setup_email = wait.until(
        EC.visibility_of_element_located((By.ID, "com.google.android.gm:id/setup_addresses_add_another")))
    elem_setup_email.click()

    elem_gmail = wait.until(EC.visibility_of_element_located((By.ID, "com.google.android.gm:id/account_setup_label")))
    elem_gmail.click()


def click_next(driver):
    driver.find_element(By.XPATH, "//android.widget.Button[@text='NEXT']").click()
