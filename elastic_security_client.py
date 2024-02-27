from kibana_client import KibanaClient

# ElasticSecurityClient class extended with methods for managing security rules, ML jobs, exception items, and exception lists

class ElasticSecurityClient(KibanaClient):
    def __init__(self, base_url, api_key=None):
        super().__init__(base_url, api_key=api_key)

    # Methods for managing security rules
    def create_rule(self, rule_data):
        # Create a security rule
        endpoint = f"{self.base_url}/api/detection_engine/rules"
        return self.http_client.post(endpoint, json=rule_data)

    def get_rule(self, rule_id):
        # Retrieve a security rule by ID
        endpoint = f"{self.base_url}/api/detection_engine/rules/_find?id={rule_id}"
        return self.http_client.get(endpoint)
    
    def get_all_rules(self):
        # Retrieve all security rules with pagination
        all_rules = []
        endpoint = f"{self.base_url}/api/detection_engine/rules/_find"
        response = self.http_client.get(endpoint)
        total_items = response.get('total', 0)
        items_per_page = response.get('perPage', 0)
        page_index = 1

        if total_items == 0:
            all_rules = response['data']
        else:
            total_pages = (total_items + items_per_page - 1) // items_per_page
            for page_index in range(1, total_pages + 1):
                endpoint = f"{self.base_url}/api/detection_engine/rules/_find?page={page_index}"
                response = self.http_client.get(endpoint)
                all_rules.extend(response['data'])
        return all_rules

    def update_rule(self, rule_id, updates):
        # Update a security rule by ID
        endpoint = f"{self.base_url}/api/detection_engine/rules/_update?id={rule_id}"
        return self.http_client.put(endpoint, json=updates)

    def delete_rule(self, rule_id):
        # Delete a security rule by ID
        endpoint = f"{self.base_url}/api/detection_engine/rules?id={rule_id}"
        return self.http_client.delete(endpoint)

    # Methods for managing ML jobs
    def create_ml_job(self, job_data):
        # Create an ML job
        endpoint = f"{self.base_url}/api/ml/jobs"
        return self.http_client.post(endpoint, json=job_data)

    def get_ml_job(self, job_id):
        # Retrieve an ML job by ID
        endpoint = f"{self.base_url}/api/ml/jobs/{job_id}"
        return self.http_client.get(endpoint)

    def update_ml_job(self, job_id, updates):
        # Update an ML job by ID
        endpoint = f"{self.base_url}/api/ml/jobs/{job_id}/_update"
        return self.http_client.put(endpoint, json=updates)

    def delete_ml_job(self, job_id):
        # Delete an ML job by ID
        endpoint = f"{self.base_url}/api/ml/jobs/{job_id}"
        return self.http_client.delete(endpoint)

    # Methods for managing exception items
    def create_exception_item(self, item_data):
        # Create an exception item
        endpoint = f"{self.base_url}/api/exception_lists/items"
        return self.http_client.post(endpoint, json=item_data)

    def get_exception_item(self, item_id):
        # Retrieve an exception item by ID
        endpoint = f"{self.base_url}/api/exception_lists/items/_find?id={item_id}"
        return self.http_client.get(endpoint)

    def update_exception_item(self, item_id, updates):
        # Update an exception item by ID
        endpoint = f"{self.base_url}/api/exception_lists/items/_update?id={item_id}"
        return self.http_client.put(endpoint, json=updates)

    def delete_exception_item(self, item_id):
        # Delete an exception item by ID
        endpoint = f"{self.base_url}/api/exception_lists/items?id={item_id}"
        return self.http_client.delete(endpoint)

    # Methods for managing exception lists
    def create_exception_list(self, list_data):
        # Create an exception list
        endpoint = f"{self.base_url}/api/exception_lists"
        return self.http_client.post(endpoint, json=list_data)

    def get_exception_list(self, list_id):
        # Retrieve an exception list by ID
        endpoint = f"{self.base_url}/api/exception_lists/_find?id={list_id}"
        return self.http_client.get(endpoint)

    def update_exception_list(self, list_id, updates):
        # Update an exception list by ID
        endpoint = f"{self.base_url}/api/exception_lists/_update?id={list_id}"
        return self.http_client.put(endpoint, json=updates)

    def delete_exception_list(self, list_id):
        # Delete an exception list by ID
        endpoint = f"{self.base_url}/api/exception_lists?id={list_id}"
        return self.http_client.delete(endpoint)
    


    def get_all_ml_jobs(self):
        # Retrieve all ML jobs with pagination
        all_jobs = []
        page_index = 1
        while (page_index - 1) * response.get('perPage', 0) < response.get('total', 0):
            endpoint = f"{self.base_url}/api/ml/jobs?page={page_index}"
            response = self.http_client.get(endpoint)
            if total_items is None:
                total_items = response['total']
            all_jobs.extend(response['jobs'])
            page_index += 1
        return all_jobs

    def get_all_exception_items(self):
        # Retrieve all exception items with pagination
        all_items = []
        page_index = 1
        while (page_index - 1) * response.get('perPage', 0) < response.get('total', 0):
            endpoint = f"{self.base_url}/api/exception_lists/items/_find?page={page_index}"
            response = self.http_client.get(endpoint)
            if total_items is None:
                total_items = response['total']
            all_items.extend(response['data'])
            page_index += 1
        return all_items

    def get_all_exception_lists(self):
        # Retrieve all exception lists with pagination

        
        all_lists = []
        page_index = 1
        while (page_index - 1) * response.get('perPage', 0) < response.get('total', 0):
            endpoint = f"{self.base_url}/api/exception_lists/_find?page={page_index}"
            response = self.http_client.get(endpoint)
            if total_items is None:
                total_items = response['total']
            all_lists.extend(response['data'])
            page_index += 1
        return all_lists