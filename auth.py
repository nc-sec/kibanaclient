import requests
from config import ConfigLoader

class Authenticator:
    """Handles authentication with basic auth or an API key."""
    
    def __init__(self, config_loader: ConfigLoader):
        self.config = config_loader.config
        self.session = requests.Session()

    def login(self):
        """Logs in to Elastic Cloud or on-premise instances."""
        auth_type = self.config.get('auth_type')
        if auth_type == 'basic':
            self.session.auth = (self.config['username'], self.config['password'])
        elif auth_type == 'api_key':
            self.session.headers.update({'Authorization': f"ApiKey {self.config['api_key']}"})
        else:
            raise ValueError("Unsupported authentication type")

        # Perform login to get session cookie
        login_url = self.config['kibana_url'] + '/api/security/v1/login'
        response = self.session.post(login_url)
        response.raise_for_status()  # Raise an error if login failed