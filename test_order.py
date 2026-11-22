import time

from playwright.sync_api import Page, expect


def test_place_order(page: Page):
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
    page.get_by_label("Password").fill("432443")
    page.locator("#days").select_option("10")
    page.locator("#months").select_option("May")
    page.locator("#years").select_option("1997")
    page.get_by_label("First name *").fill("Ivan")
    page.get_by_label("Last name *").fill("Ivanov")
    page.get_by_label("Company", exact=True).fill("alfa")
    page.get_by_label("Address * (Street address, P.O. Box, Company name, etc.)").fill("ula 54")
    page.locator("#country").select_option("Canada")
    page.get_by_label("State *").fill("Ontario")
    page.get_by_label("City").fill("Toronto")
    page.locator("#zipcode").fill("420")
    page.get_by_label("Mobile Number *").fill("7893421")
    page.get_by_role("radio", name="Mr.").check()
    page.get_by_role("checkbox", name="Sign up for our newsletter!").check()
    page.get_by_role("button", name="Create Account").click()
    expect(page.get_by_text("Account Created")).to_be_visible()
    page.get_by_role("link", name="Continue").click()
    expect(page.get_by_text("Logged in as")).to_be_visible()
    page.get_by_role("link", name="Products").click()
    page.locator("a[href='#Men']").click()
    page.locator("a[href='/category_products/6']").click()
    page.locator(".single-products").filter(has_text="Regular Fit Straight Jeans").locator(".add-to-cart").first.click()
    page.get_by_role("button", name="Continue shopping").click()
    page.locator("a[href='#Men']").click()
    page.locator("a[href='/category_products/3']").click()
    page.locator(".single-products").filter(has_text="Pure Cotton Neon Green Tshirt").locator(".add-to-cart").first.click()
    page.get_by_role("button", name="Continue shopping").click()
    page.get_by_role("link", name=" Cart",exact=True).click()
    expect(page.get_by_text("Pure Cotton Neon Green Tshirt")).to_be_visible()
    expect(page.get_by_text("Regular Fit Straight Jeans")).to_be_visible()
    page.locator(".check_out").filter(has_text="Proceed To Checkout").click()
    expect(page.get_by_text("Review Your Order")).to_be_visible()
    expect(page.get_by_text("Total Amount")).to_be_visible()
    page.locator(".form-control").fill("Thank you,for your products")
    page.locator(".check_out").filter(has_text="Place Order").click()
    expect(page.get_by_role("heading",name="Payment")).to_be_visible()
    page.locator("input[data-qa='name-on-card']").fill("IVAN IVANOV")
    page.locator("input[data-qa='card-number']").fill("43827293844739281238")
    page.locator("input[data-qa='cvc']").fill("391")
    page.locator("input[data-qa='expiry-month']").fill("11")
    page.locator("input[data-qa='expiry-year']").fill("2029")
    page.get_by_role("button", name="Pay and Confirm Order").click()
    expect(page.get_by_text("Order Placed!")).to_be_visible()
    page.locator("a[data-qa='continue-button']").click()
    page.locator("a[href='/delete_account']").click()
    expect(page.get_by_text("Account Deleted")).to_be_visible()












