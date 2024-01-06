# Gmail App Login Form Quality

This project automates the testing of the Gmail app's login form using Appium, pytest, and an Android emulator from Android Studio. It is designed to validate both positive and negative authentication flows.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Android Studio is installed with the latest SDK and tools.
- Python 3.9 or above is installed on your machine.
- Appium is installed and configured correctly.

## Setup

Follow these steps to set up your environment for running the automated tests:

### Create an Android Emulator

1. Open Android Studio and navigate to the **AVD Manager**.
2. Click on **Create Virtual Device**.
3. Select a device definition and click **Next**.
4. Choose a system image with Android version **11.0 (R)** and download it if necessary.
5. Complete the AVD configuration and click **Finish**.

### Install Dependencies

Install all required dependencies by running the following command in the root directory of the project:

```bash
pip install -r requirements.txt
```
### Verify Emulator is Running

Before running the tests, ensure that the Android Emulator is up and running:

1. Start the Android Emulator through the AVD Manager in Android Studio or by using the command line:

   ```bash
   emulator -avd <Your_AVD_Name>
    ```
   
Confirm that the emulator is listed in the connected devices:
```bash
adb devices
```
### Verify Appium Server is Running
1. Start the Appium server. You can do this via the Appium Desktop client or by running the following command:
```bash
appium
```
2. Ensure that the server is listening on the default port **4723**.
____________________________________________________________________________
# Executing Tests
With the emulator and Appium server running, execute the automated tests by running the following command:
```bash
pytest
```

   