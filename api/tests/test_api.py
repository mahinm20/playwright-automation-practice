from api_helpers.api_helpers import APIHelpers
from common_utils.generate_data import BookingData

def test_get_booking(api_context_setup):
    api = APIHelpers(api_context_setup)
    response = api.get("/booking")
    assert response.status == 200

def test_get_booking_id(api_context_setup):
    api = APIHelpers(api_context_setup)
    response = api.get(f"/booking/4")
    print(response.json())
    assert response.status == 200

def test_create_booking(api_context_setup):
    api = APIHelpers(api_context_setup)
    data_generator = BookingData()
    payload = data_generator.generate_booking()
    response = api.post("/booking",data=payload)
    print(response.json()['booking'])
    print(payload)
    assert response.status == 200
    assert payload == response.json()['booking']

def test_update_entire_booking(api_context_setup,get_auth_token):
    api = APIHelpers(api_context_setup)
    header={
        "Cookie": get_auth_token
        }
    data_generator = BookingData()
    payload = data_generator.generate_booking()
    response = api.put(f"/booking/4",data=payload,headers=header)
    print(response.json())
    print(payload)
    assert response.status == 200
    assert payload == response.json()

def test_update_partially(api_context_setup,get_auth_token):
    api = APIHelpers(api_context_setup)
    header={
        "Cookie": get_auth_token
        }
    payload = {"firstname":"Mahin"}
    response = api.patch(f"/booking/4",data=payload,headers=header)
    print(response.json())
    print(payload)
    assert response.status == 200
    assert payload['firstname'] == response.json()['firstname']

def test_create_and_delete_booking(api_context_setup,get_auth_token):
    api = APIHelpers(api_context_setup)
    data_generator = BookingData()
    payload = data_generator.generate_booking()
    response = api.post("/booking",data=payload)
    bookingid=(response.json()['bookingid'])
    header={
        "Cookie": get_auth_token
        }
    response = api.delete(f"/booking/{bookingid}",headers=header)
    assert response.status == 201
    






# import pytest
# import json 
# from playwright.sync_api import sync_playwright


# BASE_URL = "https://restful-booker.herokuapp.com"

# @pytest.fixture
# def test_auth():
#     with sync_playwright() as p:
#         request_context = p.request.new_context()
#         url = BASE_URL+"/auth"
#         data = {
#         "username" : "admin",
#         "password" : "password123"
#         }
#         response=request_context.post(url=url,data=data)
#         token = (response.json()['token'])
#         print(f"Authentication Token : {token}")
#         return token

# def test_get():
#     with sync_playwright() as p:
#         request_context = p.request.new_context()
#         url = BASE_URL+"/booking"
#         response=request_context.get(url=url)
#         print(response.json())

# def test_booking_id():

#     with sync_playwright() as p:
#         url = BASE_URL+"/booking/3886"
#         request_context = p.request.new_context()
#         response=request_context.get(url=url)
#         print(response.json())

# def test_create_booking():
#     with sync_playwright() as p:
#         request_context = p.request.new_context()
#         url = BASE_URL+"/booking"
#         data = {
#             "firstname" : "Mahin",
#             "lastname" : "Malhotra",
#             "totalprice" : 1234,
#             "depositpaid" : True,
#             "bookingdates" : {
#                 "checkin" : "2019-01-01",
#                 "checkout" : "2019-01-02"
#             },
#             "additionalneeds" : "Breakfast"
#         }
#         response=request_context.post(url=url,data=data)
#         print(response.json())
#         return response.json()['bookingid']

# def test_put_update(test_auth,id=299):
    
#     with sync_playwright() as p:
#         request_context = p.request.new_context()
#         url = f"{BASE_URL}/booking/{id}"
#         data = {
#             "firstname" : "Kunal",
#             "lastname" : "Sharma",
#             "totalprice" : 6969,
#             "depositpaid" : False,
#             "bookingdates" : {
#                 "checkin" : "2019-01-01",
#                 "checkout" : "2019-01-02"
#             },
#             "additionalneeds" : "Extra Large Mattress"
#         }
        
#         header={
#         "Cookie": f"token={test_auth}"
#         # "Content-Type": "application/json",
#         # "Accept": "application/json",
#         }
#         response=request_context.put(url=url,data=data,headers=header)
#         print(response.json())


# def test_patch(test_auth, id=299):
#     with sync_playwright() as p:
#         request_context = p.request.new_context()
#         url = f"{BASE_URL}/booking/{id}"
#         data = {
#             "firstname": "Chaitanya",
#             "additionalneeds": "Early Checkin"
#         }
        
#         headers = {
#             "Cookie": f"token={test_auth}",
#             "Content-Type": "application/json",
#             "Accept": "application/json"
#         }

#         response = request_context.patch(
#             url=url,
#             data=data,
#             headers=headers
#         )

#         print(response.json())
        

        
# def test_delete_booking(test_auth):
#     id=test_create_booking()
#     with sync_playwright() as p:
#         headers = {
#             "Cookie": f"token={test_auth}",
#             "Content-Type": "application/json"
#         }
#         url = f"{BASE_URL}/booking/{id}"
#         request_context = p.request.new_context()
#         response=request_context.delete(url=url,headers=headers)
#         print(response)
