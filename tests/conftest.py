import os

import allure
import allure_commons
import pytest
from appium import webdriver
from selene import browser, support

from config import to_driver_options, config
from qa_guru_python_07_22.utils.allure_utils import (
    attach_bstack_screenshot,
    attach_bstack_page_source,
    attach_bstack_video,
)


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = to_driver_options()
    with allure.step('Init app session'):
        browser.config.driver = webdriver.Remote(config.remote_url, options=options)

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    session_id = browser.driver.session_id

    attach_bstack_screenshot(browser)
    attach_bstack_page_source(browser)

    with allure.step('End app session'):
        browser.quit()

    if config.context == 'bstack':
        attach_bstack_video(session_id)
