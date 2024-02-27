class ExceptionLists:
    """Interacts with Exception Lists and Items in the Kibana API."""
    
    def __init__(self, session):
        self.session = session

    def get_exception_items(self, params=None):
        """Gets exception list items with support for pagination."""
        response = self.session.get('/api/exception_lists/items', params=params)
        response.raise_for_status()
        return response.json()

    def create_exception_item(self, data):
        """Creates a new exception list item."""
        response = self.session.post('/api/exception_lists/items', json=data)
        response.raise_for_status()
        return response.json()

    def update_exception_item(self, item_id, data):
        """Updates an existing exception list item."""
        response = self.session.put(f'/api/exception_lists/items/{item_id}', json=data)
        response.raise_for_status()
        return response.json()

    def delete_exception_item(self, item_id):
        """Deletes an exception list item."""
        response = self.session.delete(f'/api/exception_lists/items/{item_id}')
        response.raise_for_status()
        return response.json()