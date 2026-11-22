import random
import time

import pytest
import requests
from faker import Faker
from login_page import LoginPage
from payment_page import PaymentPage
from playwright.sync_api import Page, expect


@pytest.fixture
def reg(page: Page):
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    company = fake.company()
    address = fake.address()
    country = random.choice(['India', 'United States', 'Canada', 'Australia', 'Israel', 'New Zealand', 'Singapore'])
    city = fake.city()
    state = fake.state()
    zipcode = str(random.randint(111111,999999))
    days = str(random.randint(1,28))
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    month = random.choice(months)
    years = str(random.randint(1990,2000))
    number = str(random.randint(711111111,799999999))

    email = f"ivan.test{int(time.time())}@gmail.com"
    password = "Test12345"


    api_response = requests.post(
        "https://automationexercise.com/api/createAccount",
        data={
            "name": first_name,
            "email": email,
            "password": password,
            "title": "Mr",
            "birth_date": days,
            "birth_month": month,
            "birth_year": years,
            "firstname": first_name,
            "lastname": last_name,
            "company": company,
            "address1": address,
            "address2": "",
            "country": country,
            "zipcode": zipcode,
            "state": state,
            "city": city,
            "mobile_number": number,
        },
    )
    assert api_response.json()["responseCode"] == 201

    page.goto("https://automationexercise.com/")
    if page.locator(".fc-cta-consent").is_visible():
        page.locator(".fc-cta-consent").click()
    page.get_by_role("link", name=" Signup / Login").click()
    page.locator("input[data-qa='login-email']").fill(email)
    page.locator("input[data-qa='login-password']").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Logged in as")).to_be_visible()


    yield email, password
    requests.delete(
        "https://automationexercise.com/api/deleteAccount",
        data={"email": email, "password": password},
        timeout=30,
    )

@pytest.fixture
def pay(page: Page):
    payment = PaymentPage(page)
    return payment

@pytest.fixture
def login_page(page: Page):
    login = LoginPage(page)
    return login

@pytest.fixture
def context(context):
    blocked = ("googlesyndication", "doubleclick", "googleadservices")
    context.route(
        "**/*",
        lambda route: route.abort()
        if any(word in route.request.url for word in blocked)
        else route.continue_(),
    )
    return context