from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.product_page import ProductPage


def test_user_can_open_shopping_cart(page):
    home_page = HomePage(page)

    home_page.open()
    home_page.open_cart()

    expect(page).to_have_url(
        "https://demowebshop.tricentis.com/cart"
    )
    expect(
        page.get_by_role("heading", name="Shopping cart")
    ).to_be_visible()


def test_user_can_add_product_to_cart(page):
    home_page = HomePage(page)
    product_page = ProductPage(page)

    home_page.open()
    home_page.search("computer")
    product_page.open_product("Simple Computer")

    product_page.configure_computer()
    product_page.add_to_cart()

    expect(
        product_page.success_message
    ).to_be_visible()

    expect(
        page.locator(".cart-qty")
    ).to_contain_text("1")