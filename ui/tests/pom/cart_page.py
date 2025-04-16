import os
from playwright.sync_api import Page
from pom.login_page import LoginPage
from common_utils.generate_data import CreditCardData

product_map = {
    "Blue Top": 0,
    "Men Tshirt": 1,
    "Sleeveless Dress": 2,
    "Stylish Dress": 3,
    "Winter Top": 4,
    "Summer White Top": 5,
    "Madame Top For Women": 6,
    "Fancy Green Top": 7,
    "Sleeves Printed Top - White": 8,
    "Half Sleeves Top Schiffli Detailing - Pink": 9,
    "Frozen Tops For Kids": 10,
    "Full Sleeves Top Cherry - Pink": 11,
    "Printed Off Shoulder Top - White": 12,
    "Sleeves Top and Short - Blue & Pink": 13,
    "Little Girls Mr. Panda Shirt": 14,
    "Sleeveless Unicorn Patch Gown - Pink": 15,
    "Cotton Mull Embroidered Dress": 16,
    "Blue Cotton Indie Mickey Dress": 17,
    "Long Maxi Tulle Fancy Dress Up Outfits -Pink": 18,
    "Sleeveless Unicorn Print Fit & Flare Net Dress - Multi": 19,
    "Colour Blocked Shirt – Sky Blue": 20,
    "Pure Cotton V-Neck T-Shirt": 21,
    "Green Side Placket Detail T-Shirt": 22,
    "Premium Polo T-Shirts": 23,
    "Pure Cotton Neon Green Tshirt": 24,
    "Soft Stretch Jeans": 25,
    "Regular Fit Straight Jeans": 26,
    "Grunt Blue Slim Fit Jeans": 27,
    "Rose Pink Embroidered Maxi Dress": 28,
    "Cotton Silk Hand Block Print Saree": 29,
    "Rust Red Linen Saree": 30,
    "Beautiful Peacock Blue Cotton Linen Saree": 31,
    "Lace Top For Women": 32,
    "GRAPHIC DESIGN MEN T SHIRT - BLUE": 33
}


class CartPage(LoginPage):
    def __init__(self,page:Page):
        super().__init__(page)
        self.page = page
    
    def add_item_to_cart(self,product_name):
        products = self.page.locator('.features_items .product-image-wrapper')
        target_product = products.nth(product_map[product_name])
        target_product.hover()
        target_product.locator(".product-overlay a.add-to-cart").click()

    def proceed_to_checkout(self):    
        self.page.wait_for_selector('#cartModal')
        self.page.locator('#cartModal').get_by_role('link', name='View Cart').click()
        self.page.get_by_text('Proceed To Checkout').click()

    def continue_shopping(self):
        self.page.get_by_role("button", name="Continue Shopping").click()

    
    def place_order(self):    
        self.page.get_by_role("link", name="Place Order").click()

    def do_payment(self):
        credit_card=CreditCardData()
        credit_card_data =  credit_card.get_card_details()    
        self.page.locator("input[data-qa='name-on-card']").fill(credit_card_data['name'])
        self.page.locator("input[data-qa='card-number']").fill(credit_card_data['number'])
        self.page.locator("input[data-qa='cvc']").fill(credit_card_data['cvv'])
        self.page.locator("input[data-qa='expiry-month']").fill(credit_card_data['expiry_month'])
        self.page.locator("input[data-qa='expiry-year']").fill(credit_card_data['expiry_year'])
        self.page.locator("#submit").click()
    
    def verify_success(self):
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        self.page.screenshot(path="screenshots/order_success.png")  
        return self.page.get_by_text("Congratulations! Your order has been confirmed!").is_visible()
