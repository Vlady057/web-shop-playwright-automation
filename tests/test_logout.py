from datetime import datetime

from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.register_page import RegisterPage


def test_user_can_logout_after_registration(page):
    register_page = RegisterPage(page)
    login_page = LoginPage(page)

    unique_email = (
        f"volodymyr_{datetime.now().strftime('%Y%m%d%H%M%S%f')}"
        "@example.com"
    )

    register_page.open()
    register_page.register(
        first_name="Volodymyr",
        last_name="Test",
        email=unique_email,
        password="TestPassword123!"
    )

    expect(
        page.locator(".result")
    ).to_have_text("Your registration completed")

    login_page.logout()

    expect(
        page.get_by_role("link", name="Log in")
    ).to_be_visible()