import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be, have


def test_search_for_appium():
    with allure.step('Click on Skip button'):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")
        ).click()

    with allure.step('Search for "Appium"'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
            'Appium'
        )
    with allure.step('Search results should contain "Appium"'):
        results = browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        )
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


def test_search_and_open_article_for_testing():
    with allure.step('Click on Skip button'):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")
        ).click()

    with allure.step('Search for "Selene"'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
            'Selene'
        )
    with allure.step('Open the first article'):
        results = browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        )
        results.first.click()

    with allure.step('Article title should be "Selene"'):
        browser.element((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(
            have.exact_text('Selene')
        )


def test_onboarding_screens():
    continue_button = browser.element(
        (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')
    )
    title = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))

    with allure.step('Click on Continue button'):
        continue_button.click()
    with allure.step('Verify the page title is "New ways to explore"'):
        title.should(have.exact_text('New ways to explore'))

    with allure.step('Click on Continue button'):
        continue_button.click()
    with allure.step('Verify the page title is "Reading lists with sync"'):
        title.should(have.exact_text('Reading lists with sync'))

    with allure.step('Click on Continue button'):
        continue_button.click()
    with allure.step('Verify the page title is "Send anonymous data"'):
        title.should(have.exact_text('Send anonymous data'))

    with allure.step('Click on Accept button'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/acceptButton')).click()
    with allure.step('Verify the main page is opened'):
        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/main_toolbar_wordmark')
        ).should(be.visible)
