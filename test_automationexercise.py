import time

from playwright.sync_api import Page, expect


def test_register_user(page:Page):
    page.goto("https://automationexercise.com/")
    if page.locator(".fc-cta-consent").is_visible():
        page.locator(".fc-cta-consent").click()
    page.get_by_role("link", name="Signup").click()
    expect(page).to_have_url(
        "https://automationexercise.com/login")
    page.get_by_placeholder("Name").fill("Ivan")
    email = f"ivan.test{int(time.time())}@gmail.com"
    page.locator("input[data-qa='signup-email']").fill(email)
    page.get_by_role("button", name="Signup").click()
    expect(page.get_by_text("enter account information")).to_be_visible()
    page.get_by_label("Password").fill("Test12345")
    page.locator("#days").select_option("10")
    page.locator("#months").select_option("May")
    page.locator("#years").select_option("1998")
    page.get_by_label("First name").fill("Ivan")
    page.get_by_label("Last name").fill("Ivanov")
    page.get_by_label("Company", exact=True).fill("Alfa")
    page.get_by_label("Address * (Street address, P.O. Box, Company name, etc.)", exact=True).fill("lenina 1")
    page.locator("#country").select_option("Canada")
    page.get_by_label("State").fill("Ontario")
    page.get_by_label("City").fill("Toronto")
    page.locator("#zipcode").fill("44545")
    page.get_by_label("Mobile number").fill("12345")
    page.get_by_role("button", name="Create account").click()
    expect(page.get_by_text("Account created")).to_be_visible()
    page.get_by_role("link", name="Continue").click()
    expect(page.get_by_text("Logged in as")).to_be_visible()
    page.get_by_role("link", name="Delete Account").click()
    expect(page.get_by_text("Account deleted")).to_be_visible()

    page.get_by_role("link", name=" Products").click()
    page.locator(".single-products").filter(has_text="Rs. 850 Pure Cotton Neon Green Tshirt").locator(
        ".add-to-cart").first.click()

