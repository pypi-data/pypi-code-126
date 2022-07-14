from cqase.api.attachments import AttachmentsApi
from cqase.api.cases import CasesApi
from cqase.api.custom_fields import CustomFieldsApi
from cqase.api.defects import DefectsApi
from cqase.api.environments import EnvironmentsApi
from cqase.api.milestones import MilestoneApi
from cqase.api.plans import PlansApi
from cqase.api.projects import ProjectsApi
from cqase.api.results import ResultsApi
from cqase.api.runs import RunsApi
from cqase.api.shared_steps import SharedStepsApi
from cqase.api.suites import SuitesApi
from cqase.request import Client


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
        self.plans = PlansApi(self)
        self.runs = RunsApi(self)
        self.results = ResultsApi(self)
        self.shared_steps = SharedStepsApi(self)
        self.suites = SuitesApi(self)
