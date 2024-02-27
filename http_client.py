import requests
from exceptions import HTTPRequestException

# HTTPClient class updated to include GET, PUT, and DELETE methods

class HTTPClient:
    def __init__(self, auth):
        self.auth = auth

    def get(self, url):
        # Method to send a GET request
        try:
            response = requests.get(url, headers=self.auth.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise HTTPRequestException(e)

    def post(self, url, json):
        # Method to send a POST request
        try:
            response = requests.post(url, json=json, headers=self.auth.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise HTTPRequestException(e)

    def put(self, url, json):
        # Method to send a PUT request
        try:
            response = requests.put(url, json=json, headers=self.auth.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise HTTPRequestException(e)

    def delete(self, url):
        # Method to send a DELETE request
        try:
            response = requests.delete(url, headers=self.auth.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise HTTPRequestException(e)