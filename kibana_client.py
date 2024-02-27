from http_client import HTTPClient
from auth import Auth

class KibanaClient:
    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        self.auth = Auth(api_key=api_key)
        self.http_client = HTTPClient(self.auth)

    def search(self, index, query):
        # Method to search in a Kibana index
        endpoint = f"{self.base_url}/api/console/proxy?path=/{index}/_search&method=POST"
        data = {"query": query}
        return self.http_client.post(endpoint, json=data)

    # Additional methods to interact with Kibana API
    # ...