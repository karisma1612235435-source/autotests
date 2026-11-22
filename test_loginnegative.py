from playwright.sync_api import Page, expect

def test_negative_log(page: Page, reg: tuple[str, str], login_page):

    email,password=reg

    login_page.logout() 
    login_page.login(email,password + "wrong")
    login_page.check_login_error()
    login_page.login(email,password)



