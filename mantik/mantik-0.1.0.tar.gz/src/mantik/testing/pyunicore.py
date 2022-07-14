import io
import typing as t


class FakeTransport:
    def __init__(self, auth_token: str = "test_token", oidc: bool = True):
        self.auth_token = auth_token
        self.oidc = oidc


class FakeJob:
    def __init__(
        self,
        transport: FakeTransport,
        job_url: str = "test-job",
        properties: t.Dict = None,
        existing_files: t.Dict[str, str] = None,
        will_be_successful: bool = True,
    ):
        self.transport = transport
        self.url = job_url
        self._properties = properties or {"status": "QUEUED"}
        self._existing_files = existing_files or {}
        self._successful = will_be_successful
        self.working_dir = FakeWorkDir()
        self.started = False

    @property
    def properties(self) -> t.Dict:
        return self._properties

    @property
    def job_id(self) -> str:
        return self.url

    def poll(self) -> None:
        self._properties["status"] = (
            "SUCCESSFUL" if self._successful else "FAILED"
        )

    def abort(self) -> None:
        pass

    def start(self) -> None:
        self.started = True


class FakeWorkDir:

    DEFAULT_FILES = ["stdout", "stderr", "mantik.log"]

    def __init__(self, files: t.Optional[t.List[str]] = None):
        self.directory = "."
        self._files = files or self.DEFAULT_FILES

    @property
    def properties(self):
        return {"foo": "bar"}

    def listdir(self):
        return self._files

    def stat(self, filename):
        return FakeFileReference(content=f"Stat {filename}")


class FakeFileReference:
    def __init__(self, content: str):
        self._content = content

    def raw(self):
        return io.StringIO(self._content)


class FakeClient:
    def __init__(
        self,
        transport: FakeTransport = None,
        site_url: str = "test_api_url",
        login_successful: bool = False,
    ):
        if transport is None:
            transport = FakeTransport()
        self.transport = transport
        self.site_url = site_url
        self._properties = {"client": {"xlogin": {}}}
        if login_successful:
            self.add_login_info({"test_login": "test_logged_in"})

    @property
    def properties(self) -> t.Dict:
        return {**self.__dict__, **self._properties}

    def add_login_info(self, login: t.Dict) -> None:
        self._properties["client"]["xlogin"] = login

    def new_job(self, job_description: t.Dict, inputs: t.List) -> FakeJob:
        return FakeJob(transport=self.transport, job_url="test_job_url")
