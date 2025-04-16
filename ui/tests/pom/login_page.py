from playwright.sync_api import Page
LOGIN_URL = "https://automationexercise.com/login"

class LoginPage:

    def __init__(self,page:Page):
        self.page = page
        self.url = LOGIN_URL

    def open_login_url(self):
        self.page.goto(self.url)

    def enter_credentials(self,username,password):
        self.page.locator("input[data-qa='login-email']").fill(username)
        self.page.locator("input[data-qa='login-password']").fill(password)

    def login(self):
        login_button = self.page.get_by_role("button", name="Login")
        login_button.wait_for()
        login_button.click()      

    def verify_login(self):
        return self.page.locator("a[href='/logout']").is_visible()      

