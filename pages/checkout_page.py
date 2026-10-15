from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.get_by_role(
            "button",
            name="Checkout"
        )
        self.continue_buttons = page.get_by_role(
            "button",
            name="Continue"
        )
        self.confirm_order_button = page.get_by_role(
            "button",
            name="Confirm"
        )

    def start_checkout(self):
        self.checkout_button.click()

    def continue_step(self, index: int):
        self.continue_buttons.nth(index).click()

    def confirm_order(self):
        self.confirm_order_button.click()