from playwright.sync_api import expect

from pages.home_page import HomePage


def test_user_can_search_for_product(page):
    home_page = HomePage(page)

    home_page.open()
    home_page.search("computer")

    expect(page).to_have_url(
        "https://demowebshop.tricentis.com/search?q=computer"
    )

    expect(
        page.locator(".product-item")
    ).to_have_count(4)


def test_search_with_no_matching_products(page):
    home_page = HomePage(page)

    home_page.open()
    home_page.search("xyznonexistentproduct987654")

    expect(
        page.get_by_text(
            "No products were found that matched your criteria.",
            exact=True
        )
    ).to_be_visible()