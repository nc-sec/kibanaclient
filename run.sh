# a) Install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# b) Set environment variables for Elastic Cloud ID and API Key
export ELASTIC_CLOUD_ID="your_elastic_cloud_id"
export ELASTIC_API_KEY="your_elastic_api_key"

# c) Run all necessary parts of the codebase
python entrypoint.py &
