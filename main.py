import pytest
from appium_config import get_appium_capabilities
from appium import webdriver


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


if __name__ == "__main__":
    # Run pytest to discover and execute test cases
    pytest.main(["-v", "test_positive.py", "test_negative.py"])
