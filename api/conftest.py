import pytest 
from playwright.sync_api import sync_playwright

BASE_URL = "https://restful-booker.herokuapp.com"

@pytest.fixture(scope="function")
def api_context_setup():
    with sync_playwright() as p:
        request_context = p.request.new_context(base_url=BASE_URL)
        yield request_context
        request_context.dispose()

@pytest.fixture(scope="session")
def get_auth_token():
    with sync_playwright() as p:
        request_context = p.request.new_context()
        url = BASE_URL+"/auth"
        data = {
        "username" : "admin",
        "password" : "password123"
        }
        response=request_context.post(url=url,data=data)
        token = (response.json()['token'])
        print(f"Authentication Token : {token}")
        return f"token={token}"