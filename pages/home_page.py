from playwright.sync_api import Page


class HomePage:
    URL = "https://demowebshop.tricentis.com/"

    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator("#small-searchterms")
        self.search_button = page.get_by_role("button", name="Search")
        self.cart_link = page.locator("a.ico-cart").last

    def open(self):
        self.page.goto(self.URL)

    def search(self, product: str):
        self.search_input.fill(product)
        self.search_button.click()

    def open_cart(self):
        self.cart_link.click()