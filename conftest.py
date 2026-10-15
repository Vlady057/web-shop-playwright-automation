import pytest
from playwright.sync_api import Page


@pytest.fixture
def demo_page(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    return page