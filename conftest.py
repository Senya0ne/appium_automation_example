import pytest as pytest
from appium import webdriver


@pytest.fixture
def driver():
    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "11",
        "automationName": "Appium",
        "deviceName": "TestAndroid",
        "app": "/Users/svasilchenko/PycharmProjects/PythonAppiumAutomation/apks/org.wikipedia.apk",
        "packageName": "org.wikipedia/org.wikipedia.main.MainActivity"
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
    driver.quit()
