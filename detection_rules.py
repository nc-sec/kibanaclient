class DetectionRules:
    """Interacts with Detection Rules in the Kibana API."""
    
    def __init__(self, session):
        self.session = session

    def get_rules(self, params=None):
        """Gets detection rules with support for pagination."""
        response = self.session.get('/api/detection_engine/rules', params=params)
        response.raise_for_status()
        return response.json()

    def create_rule(self, data):
        """Creates a new detection rule."""
        response = self.session.post('/api/detection_engine/rules', json=data)
        response.raise_for_status()
        return response.json()

    def update_rule(self, rule_id, data):
        """Updates an existing detection rule."""
        response = self.session.put(f'/api/detection_engine/rules/{rule_id}', json=data)
        response.raise_for_status()
        return response.json()

    def delete_rule(self, rule_id):
        """Deletes a detection rule."""
        response = self.session.delete(f'/api/detection_engine/rules/{rule_id}')
        response.raise_for_status()
        return response.json()

    def get_tags(self):
        """Aggregates and returns rule tags."""
        response = self.session.get('/api/detection_engine/tags')
        response.raise_for_status()
        return response.json()

    def import_rules(self, file):
        """Imports rules from an .ndjson file."""
        files = {'file': file}
        response = self.session.post('/api/detection_engine/rules/_import', files=files)
        response.raise_for_status()
        return response.json()

    def export_rules(self):
        """Exports rules to an .ndjson file."""
        response = self.session.post('/api/detection_engine/rules/_export')
        response.raise_for_status()
        return response.content