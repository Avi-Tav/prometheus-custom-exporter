import requests

GOOGLE_API_URL = '' # An example for the endpoint, Mainly you will add somthing like /api/v1/endpoint

class MyApiManager(object):
    def __init__(self, server_uri, password, username):
        self.server_uri = server_uri
        self.session = requests.Session()
        self.session.headers = {'Content-Type': 'application/json'} # Add headers if needed
        self.password = password
        self.username = username
    
    def get_my_end_point(self): # change the name of the method to match the endpoint and add more methods if needed
        url = self.server_uri + GOOGLE_API_URL
        data = {} # Add payload if needed
        response = self.session.get(url) # Adding a payload: response = self.session.get(url, json=data)
        return response.status_code