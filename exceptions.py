class HTTPRequestException(Exception):
    """Exception raised for errors in the HTTP request."""
    def __init__(self, original_exception):
        self.original_exception = original_exception
        super().__init__(str(original_exception))