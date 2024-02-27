import os
from kibana_client import KibanaClient
from elastic_security_client import ElasticSecurityClient

# Entry point for the client library
def main():
    # Example usage of the KibanaClient and ElasticSecurityClient
    elastic_cloud_id = os.getenv('ELASTIC_CLOUD_ID')
    api_key = os.getenv('ELASTIC_API_KEY')
    kibana_url = f'https://{elastic_cloud_id}.kibana.elastic-cloud.com'
    kibana_client = KibanaClient(kibana_url, api_key=api_key)
    elastic_security_client = ElasticSecurityClient(kibana_url, api_key=api_key)

    # Perform actions with the clients
    # ...

if __name__ == "__main__":
    main()