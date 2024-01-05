from appium import webdriver
import pytest

def setup_function(function):
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Android Emulator',
        'appPackage': 'com.google.android.gm',  # Gmail package name
        'appActivity': '.ConversationListActivityGmail',  # Gmail activity name
        'noReset': True
    }
    global driver
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

def teardown_function(function):
    driver.quit()

def test_open_gmail():
    # Your code to navigate and assert conditions
    pass

if __name__ == "__main__":
    pytest.main()
