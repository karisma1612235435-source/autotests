from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self,page: Page):
            self.page = page
    def login(self, email: str, password: str) -> None:
        self.page.goto("https://automationexercise.com/")
        if self.page.locator(".fc-cta-consent").is_visible():
            self.page.locator(".fc-cta-consent").click()
        self.page.get_by_role("link", name=" Signup / Login").click()
        self.page.locator("input[data-qa='login-email']").fill(email)
        self.page.locator("input[data-qa='login-password']").fill(password)
        self.page.get_by_role("button", name="Login").click()
        
    def logout(self):
        self.page.locator("a[href='/logout']").click()


    def check_login_error(self):
        expect(self.page.get_by_text("Your email or password is incorrect!")).to_be_visible()