from playwright.sync_api import Page


class LoginPage:
    URL = "https://demowebshop.tricentis.com/login"

    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("#Email")
        self.password_input = page.locator("#Password")
        self.login_button = page.get_by_role(
            "button",
            name="Log in"
        )
        self.logout_link = page.get_by_role(
            "link",
            name="Log out"
        )
        self.validation_errors = page.locator(
            ".validation-summary-errors"
        )

    def open(self):
        self.page.goto(self.URL)

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def logout(self):
        self.logout_link.click()