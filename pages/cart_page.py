from playwright.sync_api import Page


class CartPage:
    URL = "https://demowebshop.tricentis.com/cart"

    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart-item-row")
        self.empty_cart_message = page.locator(".order-summary-content")

    def open(self):
        self.page.goto(self.URL)

    def remove_first_item(self):
        self.cart_items.first.locator(
            "input[name*='removefromcart']"
        ).check()
        self.page.get_by_role(
            "button",
            name="Update shopping cart"
        ).click()