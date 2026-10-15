from playwright.sync_api import Page


class RegisterPage:
    URL = "https://demowebshop.tricentis.com/register"

    def __init__(self, page: Page):
        self.page = page
        self.male_radio = page.locator("#gender-male")
        self.first_name = page.locator("#FirstName")
        self.last_name = page.locator("#LastName")
        self.email = page.locator("#Email")
        self.password = page.locator("#Password")
        self.confirm_password = page.locator("#ConfirmPassword")
        self.register_button = page.get_by_role(
            "button",
            name="Register"
        )
        self.registration_result = page.locator(
            ".result"
        )

    def open(self):
        self.page.goto(self.URL)

    def register(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str
    ):
        self.male_radio.check()
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.email.fill(email)
        self.password.fill(password)
        self.confirm_password.fill(password)
        self.register_button.click()