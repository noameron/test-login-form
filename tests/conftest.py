import subprocess

import pytest
from appium import webdriver


def get_device_name():
    """
    Get device name
    :return:
    """
    result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, text=True)
    lines = result.stdout.splitlines()
    for line in lines[1:]:
        if "\tdevice" in line:
            return line.split("\t")[0]
    raise RuntimeError("No device found")


def get_platform_version(device_name):
    """
    Get platform version of the device
    :param device_name:
    :return:
    """
    cmd = f"adb -s {device_name} shell getprop ro.build.version.release"
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True, shell=True)
    return result.stdout.strip()


def get_appium_capabilities():
    device_name = get_device_name()
    platform_version = get_platform_version(device_name)
    capabilities = {
        'platformName': 'Android',
        'platformVersion': platform_version,
        'deviceName': device_name,
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

