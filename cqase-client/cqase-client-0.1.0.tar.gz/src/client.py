from src.api.attachments import AttachmentsApi
from src.api.cases import CasesApi
from src.api.custom_fields import CustomFieldsApi
from src.api.defects import DefectsApi
from src.api.environments import EnvironmentsApi
from src.api.milestones import MilestoneApi
from src.api.plans import PlanesApi
from src.api.projects import ProjectsApi
from src.api.results import ResultsApi
from src.api.runs import RunsApi
from src.api.shared_steps import SharedStepsApi
from src.api.suites import SuitesApi
from src.request import Client


class QaseClient:
    def __init__(self, api_token: str, base_path: str = "https://api.qase.io/v1"):
        self.client = Client(headers={"Token": api_token})
        self.base_path = base_path

        self.projects = ProjectsApi(self)
        self.cases = CasesApi(self)
        self.attachments = AttachmentsApi(self)
        self.custom_fields = CustomFieldsApi(self)
        self.defects = DefectsApi(self)
        self.environments = EnvironmentsApi(self)
        self.milestones = MilestoneApi(self)
        self.planes = PlanesApi(self)
        self.runs = RunsApi(self)
        self.results = ResultsApi(self)
        self.shared_steps = SharedStepsApi(self)
        self.suites = SuitesApi(self)
