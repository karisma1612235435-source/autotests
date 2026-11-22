
from typing import Any

from playwright.sync_api import Page, expect


def test_place_order(page: Page, reg: Any, pay: Any):
    page.locator("a[href='/products']").click()
    page.locator("a[href='#Men']").click()
    page.locator("a[href='/category_products/6']").click()
    page.locator(".single-products").filter(has_text="Grunt Blue Slim Fit Jeans").locator(".add-to-cart").first.click()
    page.get_by_role("button", name="Continue shopping").click()
    page.get_by_role("link", name=" Cart", exact=True).click()
    expect(page.get_by_text("Grunt Blue Slim Fit Jeans")).to_be_visible()
    page.locator(".check_out").filter(has_text="Proceed To Checkout").click()
    expect(page.get_by_text("Review Your Order")).to_be_visible()
    expect(page.get_by_text("Total Amount")).to_be_visible()
    page.locator(".form-control").fill("Thank you,for your products")
    page.locator(".check_out").filter(has_text="Place Order").click()
    expect(page.get_by_role("heading", name="Payment")).to_be_visible()
    pay.fill_card(name="IVAN IVANOV",card_number="3827293844739281238",cvc="391",month="11",year="2029")
    pay.pay()
    pay.check_order_placed()



