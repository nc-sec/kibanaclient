from auth import Authenticator

class SessionManager:
    """Manages the session cookie from login to perform requests."""
    
    def __init__(self, authenticator: Authenticator):
        self.session = authenticator.session

    def get_session(self):
        """Returns the current session with the authentication cookie."""
        return self.session