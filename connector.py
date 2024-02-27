from session import SessionManager
from detection_rules import DetectionRules
from exception_lists import ExceptionLists
from ml_jobs import MLJobs

class ElasticConnector:
    """Main connector class to interact with the Kibana API."""
    
    def __init__(self, session_manager: SessionManager):
        self.session = session_manager.get_session()
        self.detection_rules = DetectionRules(self.session)
        self.exception_lists = ExceptionLists(self.session)
        self.ml_jobs = MLJobs(self.session)

    # Methods to interact with the Kibana API will be added here