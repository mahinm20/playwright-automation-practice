from faker import Faker
import random
import string

class UserDataUI:
    def __init__(self, locale='en_IN'):
        self.faker = Faker(locale)

    def get_first_name(self):
        return self.faker.first_name()

    def get_last_name(self):
        return self.faker.last_name()

    def get_full_name(self):
        return self.faker.name()

    def get_address(self):
        return self.faker.address().replace("\n", ", ")

    def get_pincode(self):
        return self.faker.postcode()

    def get_city(self):
        return self.faker.city()

    def get_state(self):
        return self.faker.state()

    def get_mobile_number(self):
        return self.faker.msisdn()[-10:]

    def get_email(self):
        return self.faker.email()

    def get_dob(self, min_age=18, max_age=60):
        dob = self.faker.date_of_birth(minimum_age=min_age, maximum_age=max_age)
        return (str(dob.day), str(dob.month), str(dob.year))

    def get_password(self, length=12):
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        return password

    def get_user_data(self):
        return {
            "first_name": self.get_first_name(),
            "last_name": self.get_last_name(),
            "email": self.get_email(),
            "mobile": self.get_mobile_number(),
            "address": self.get_address(),
            "city": self.get_city(),
            "state": self.get_state(),
            "pincode": self.get_pincode(),
            "dob": self.get_dob(),
            "password": self.get_password()
        }

from faker import Faker
import random

class BookingData:
    def __init__(self):
        self.fake = Faker()

    def generate_booking(self):
        checkin_date = self.fake.date_between(start_date="-3y", end_date="-1y")
        checkout_date = self.fake.date_between(start_date=checkin_date, end_date="+1y")
        
        return {
            "firstname": self.fake.first_name(),
            "lastname": self.fake.last_name(),
            "totalprice": random.randint(50, 500),
            "depositpaid": random.choice([True, False]),
            "bookingdates": {
                "checkin": checkin_date.isoformat(),
                "checkout": checkout_date.isoformat()
            },
            "additionalneeds": random.choice(["Breakfast", "Lunch", "Late Checkout", "None"])
        }


class CreditCardData:
    def __init__(self):
        self.faker = Faker()

    def get_card_details(self):
        card_type = random.choice(['visa', 'mastercard', 'amex'])
        card = self.faker.credit_card_full(card_type)
        number = self.faker.credit_card_number(card_type)
        expiry = self.faker.credit_card_expire(start='now', end='+4y', date_format='%m/%y')
        name = self.faker.name()
        cvv = self.faker.credit_card_security_code(card_type)

        exp_month, exp_year = expiry.split('/')

        return {
            "card_type": card_type,
            "name": name,
            "number": number,
            "expiry_month": exp_month,
            "expiry_year": exp_year,
            "cvv": cvv
        }
    
