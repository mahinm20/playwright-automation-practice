from pom.login_page import LoginPage
from pom.signup_page import SignUpPage
from pom.cart_page import CartPage
from common_utils.generate_data import UserDataUI


def test_login(browser_setup):
    login_page = LoginPage(browser_setup)
    login_page.open_login_url()
    login_page.enter_credentials("mahinmalhotra20@gmail.com","mala2028")
    login_page.login()
    login_page.verify_login()

def test_already_existing_user(browser_setup):
    signup_page = SignUpPage(browser_setup)
    signup_page.open_login_url()
    user_data = {
        "first_name":"mahin",
        "email":"mahinmalhotra20@gmail.com"
    }
    signup_page.register_user(user_data)

def test_create_new_user(browser_setup):
    signup_page = SignUpPage(browser_setup)
    signup_page.open_login_url()
    user_data = UserDataUI().get_user_data()
    signup_page.register_user(user_data)

def test_checkout_using_existing_user(browser_setup):
    login_page = LoginPage(browser_setup)
    login_page.open_login_url()
    login_page.enter_credentials("mahinmalhotra20@gmail.com","mala2028")
    login_page.login()
    login_page.verify_login()
    cart_page = CartPage(browser_setup)
    cart_page.add_item_to_cart("Men Tshirt")
    cart_page.continue_shopping()
    cart_page.add_item_to_cart("Winter Top")
    cart_page.proceed_to_checkout()
    cart_page.place_order()
    cart_page.do_payment()
    assert cart_page.verify_success() == True

def test_create_user_and_checkout(browser_setup):
    signup_page = SignUpPage(browser_setup)
    signup_page.open_login_url()
    user_data = UserDataUI().get_user_data()
    signup_page.register_user(user_data)
    cart_page = CartPage(browser_setup)
    cart_page.add_item_to_cart("Men Tshirt")
    cart_page.continue_shopping()
    cart_page.add_item_to_cart("Winter Top")
    cart_page.proceed_to_checkout()
    cart_page.place_order()
    cart_page.do_payment()
    assert cart_page.verify_success() == True




