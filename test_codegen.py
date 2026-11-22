import random

from faker import Faker
from playwright.sync_api import Page, expect


def test_codegen(page: Page, reg, pay):

    page.goto("https://automationexercise.com/")
    page.get_by_role("link", name=" Products").click()
    page.get_by_role("link", name=" Men").click()
    page.get_by_role("link", name="Tshirts").click()
    page.locator(".single-products").filter(has_text="Pure Cotton V-Neck T-Shirt").locator(".add-to-cart").first.click()
    page.get_by_role("button", name="Continue Shopping").click()
    page.locator(".single-products").filter(has_text="Rs. 850 Pure Cotton Neon").locator(".add-to-cart").first.click()
    page.get_by_role("button", name="Continue Shopping").click()
    page.get_by_role("link", name=" Cart", exact=True).click()
    expect(page.locator("a[href='/product_details/28']")).to_be_visible()
    expect(page.locator("a[href='/product_details/31']")).to_be_visible()
    page.locator(".check_out").filter(has_text="Proceed To Checkout").click()
    expect(page.get_by_text("Review Your Order")).to_be_visible()
    expect(page.get_by_text("Total Amount")).to_be_visible()
    page.locator(".form-control").fill("Thank you,for your products")
    page.locator(".check_out").filter(has_text="Place Order").click()
    expect(page.get_by_role("heading", name="Payment")).to_be_visible()


    number = str(random.randint(743523134241111,799999999999999))
    cvc = str(random.randint(100,999))
    month = str(random.randint(1,12))
    year = str(random.randint(2027,2035))
    fake = Faker()
    name = fake.name()
    pay.fill_card(name=name, card_number=number, cvc=cvc, month=month, year=year)
    pay.pay()
    pay.check_order_placed()
