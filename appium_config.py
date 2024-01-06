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
