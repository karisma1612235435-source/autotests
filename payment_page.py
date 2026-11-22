from playwright.sync_api import Page, expect


class PaymentPage:
    def __init__(self,page: Page):
        self.page = page
    def fill_card(
        self,
        name: str,
        card_number: str,
        cvc: str,
        month: str,
        year: str,
    ) -> None:
        self.page.locator("input[data-qa='name-on-card']").fill(name)
        self.page.locator("input[data-qa='card-number']").fill(card_number)
        self.page.locator("input[data-qa='cvc']").fill(cvc)
        self.page.locator("input[data-qa='expiry-month']").fill(month)
        self.page.locator("input[data-qa='expiry-year']").fill(year)
    def pay(self):
        self.page.get_by_role("button", name="Pay and Confirm Order").click()
    def check_order_placed(self):
        expect(self.page.get_by_text("Order Placed!")).to_be_visible()
        # text

