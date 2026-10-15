from datetime import datetime

from playwright.sync_api import expect

from pages.register_page import RegisterPage


def test_registration_page_is_available(page):
    register_page = RegisterPage(page)

    register_page.open()

    expect(page).to_have_url(RegisterPage.URL)
    expect(
        page.get_by_role(
            "heading",
            name="Register"
        )
    ).to_be_visible()


def test_user_can_register(page):
    register_page = RegisterPage(page)

    register_page.open()

    unique_email = (
        f"volodymyr_{datetime.now().strftime('%Y%m%d%H%M%S%f')}"
        "@example.com"
    )

    register_page.register(
        first_name="Volodymyr",
        last_name="Test",
        email=unique_email,
        password="TestPassword123!"
    )

    expect(
        page.locator(".result")
    ).to_have_text("Your registration completed")