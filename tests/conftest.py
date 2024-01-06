import pytest
from appium import webdriver


def get_appium_capabilities():
    capabilities = {
        'platformName': 'Android',
        'platformVersion': '11.0',
        'deviceName': 'emulator-5554',
        'appPackage': 'com.google.android.gm',
        'appActivity': '.ConversationListActivityGmail',
        'noReset': True
    }
    return capabilities


@pytest.fixture(scope="function")
def setup_driver_capabilities(request):
    options = webdriver.webdriver.AppiumOptions()
    capabilities = get_appium_capabilities()

    for key, value in capabilities.items():
        options.set_capability(key, value)

    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', options=options)
    yield driver

    def teardown():
        driver.quit()

    request.addfinalizer(teardown)
    return driver

