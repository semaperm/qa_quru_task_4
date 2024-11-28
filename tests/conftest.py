import pytest
from selene import browser

@pytest.fixture(autouse=True)
def browser_setting():
    browser.open("https://demoqa.com/automation-practice-form")
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield

    browser.quit()