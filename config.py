import os
from typing import Literal

from appium.options.android import UiAutomator2Options
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

from qa_guru_python_07_22.utils.path import relative_from_root


class Config(BaseSettings):
    # General settings
    context: Literal['local_emulator', 'bstack'] = 'bstack'
    timeout: float = 10.0
    appWaitActivity: str = 'org.wikipedia.*'
    remote_url: str = ''
    app: str = ''

    # BrowserStack settings
    bstack_userName: str = ''
    bstack_accessKey: str = ''
    android_deviceName: str = ''
    android_platformVersion: str = ''

    # Local emulator settings
    deviceName: str = ''


load_dotenv(relative_from_root(f'.env.{Config().context}'))
config = Config()

if config.context == 'bstack':
    load_dotenv(relative_from_root('.env.credentials'))
    config.bstack_userName = os.getenv('bstack_userName')
    config.bstack_accessKey = os.getenv('bstack_accessKey')


def to_driver_options():
    options = UiAutomator2Options()

    if config.context == 'bstack':
        options.load_capabilities(
            {
                # Specify device and os_version for testing
                "platformName": 'Android',
                "platformVersion": config.android_platformVersion,
                "deviceName": config.android_deviceName,
                # Set URL of the application under test
                "app": config.app,
                'appWaitActivity': config.appWaitActivity,
                # Set other BrowserStack capabilities
                'bstack:options': {
                    "projectName": "First Python project",
                    "buildName": "browserstack-build-1",
                    "sessionName": "BStack first_test",
                    # Set your access credentials
                    "userName": config.bstack_userName,
                    "accessKey": config.bstack_accessKey,
                },
            }
        )

    elif config.context == 'local_emulator':
        app = relative_from_root(config.app)
        options.load_capabilities(
            {
                "platformName": "Android",
                "appium:automationName": "UiAutomator2",
                "deviceName": config.deviceName,
                "app": app,
                'appWaitActivity': config.appWaitActivity,
            }
        )

    return options
