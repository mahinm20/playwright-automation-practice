from playwright.sync_api import APIRequestContext
class APIHelpers:
    def __init__(self, request_context:APIRequestContext):
        self.request = request_context


    def get(self, endpoint, params=None):
        response = self.request.get(endpoint, params=params)
        return response

    def post(self, endpoint, data=None, headers=None):
        response = self.request.post(endpoint, data=data, headers=headers)
        return response

    def put(self, endpoint, data=None, headers=None):
        response = self.request.put(endpoint, data=data, headers=headers)
        return response
    
    def patch(self, endpoint, data=None, headers=None):
        response = self.request.patch(endpoint, data=data, headers=headers)
        return response

    def delete(self, endpoint, headers=None):
        response = self.request.delete(endpoint, headers=headers)
        return response
