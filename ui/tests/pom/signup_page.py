
import os
from playwright.sync_api import Page
from common_utils.generate_data import UserDataUI
LOGIN_URL = "https://automationexercise.com/login"

class SignUpPage:

    def __init__(self,page:Page):
        self.page = page
        self.url = LOGIN_URL

    def open_login_url(self):
        self.page.goto(self.url)

    def register_user(self,user_data:dict):
        self.page.locator("input[data-qa='signup-name']").fill(user_data['first_name'])
        self.page.locator("input[data-qa='signup-email']").fill(user_data['email'])
        signup_button=self.page.get_by_role("button",name="Signup")
        signup_button.wait_for()
        signup_button.click()
        if self.page.get_by_text("Email Address already exist!").is_visible():
            return 
        self.page.wait_for_selector("#id_gender1").check()
        self.page.locator("#password").fill(user_data['password'])
        dob = user_data['dob']
        day,month,year = tuple(dob)
        self.page.locator("#days").select_option(day)
        self.page.locator("#months").select_option(month)
        self.page.locator("#years").select_option(year)
        self.page.get_by_text("Sign up for our newsletter!").click()
        self.page.get_by_text("Receive special offers from our partners!").click()
        self.page.locator("input[data-qa='first_name']").fill(user_data['first_name'])
        self.page.locator("input[data-qa='last_name']").fill(user_data['last_name'])
        self.page.locator("input[data-qa='address']").fill(user_data['address'])
        self.page.locator("input[data-qa='state']").fill(user_data['state'])
        self.page.locator("input[data-qa='city']").fill(user_data['city'])
        self.page.locator("input[data-qa='zipcode']").fill(user_data['pincode'])
        self.page.locator("input[data-qa='mobile_number']").fill(user_data['mobile'])
        self.page.get_by_role("button",name='Create Account').click()
        self.page.get_by_text("Account Created!").is_visible()
        self.page.get_by_role("link",name='Continue').click()
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        self.page.screenshot(path="screenshots/user_created.png")   

    
