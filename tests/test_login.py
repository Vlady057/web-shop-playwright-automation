from playwright.sync_api import expect

from pages.login_page import LoginPage


def test_login_page_is_available(page):
    login_page = LoginPage(page)

    login_page.open()

    expect(page).to_have_url(LoginPage.URL)
    expect(
        page.get_by_role(
            "heading",
            name="Welcome, Please Sign In!"
        )
    ).to_be_visible()


def test_login_with_invalid_credentials_shows_error(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(
        email="invalid_user_qa@example.com",
        password="WrongPassword123!"
    )

    expect(
        login_page.validation_errors
    ).to_be_visible()

    expect(
        login_page.validation_errors
    ).to_contain_text("Login was unsuccessful")