from playwright.sync_api import Page


class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = page.locator(
            "#add-to-cart-button-75"
        )
        self.success_message = page.locator(
            ".bar-notification"
        )

    def open_product(self, product_name: str):
        self.page.get_by_role(
            "link",
            name=product_name,
            exact=True
        ).click()

    def configure_computer(self):
        self.page.get_by_role(
            "radio",
            name="Slow"
        ).check()

        self.page.get_by_role(
            "radio",
            name="2 GB",
            exact=True
        ).check()

        self.page.get_by_role(
            "radio",
            name="320 GB",
            exact=True
        ).check()

    def add_to_cart(self):
        self.add_to_cart_button.click()