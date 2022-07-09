import base64
import configparser
import os
from urllib.parse import urlparse

from gitlab import Gitlab


class GitProject:
    def __init__(self, token):
        self.path = GitProject.git_path()
        self.parse = GitProject.git_url_parse()
        self.branch = GitProject.get_branch()
        self.host = GitProject.git_host()
        self.url = GitProject.git_project_url()
        self.git_url = GitProject.git_url()
        self.path_with_namespace = self._get_path_with_namespace()
        self.token = token

        self._gitlab_project = None
        self._client = None
        self._master_branch = None

    @property
    def master_branch(self):
        if self._master_branch is None:
            self._master_branch = self._get_master_branch()
        return self._master_branch

    @property
    def gitlab_client(self):
        if self._client is None:
            self._client = self._get_git_client()
        return self._client

    @property
    def gitlab_project(self):
        if self._gitlab_project is None:
            self._gitlab_project = self._get_gitlab_project()
        return self._gitlab_project

    @staticmethod
    def get_branch():
        return open(os.path.join(GitProject.git_path(), 'HEAD'), 'r').read().split('heads/')[-1].strip()

    @staticmethod
    def git_path():
        current_path = os.path.abspath(os.getcwd())
        return os.path.join(current_path, '.git')

    @staticmethod
    def git_url_parse():
        config_path = os.path.join(GitProject.git_path(), 'config')
        config = configparser.ConfigParser()
        config.read(config_path)
        url = config.get('remote "origin"', "url").replace("git@", '').replace(":", "/")
        url = 'http://' + url if "http" not in url else url
        parse = urlparse(url)
        return parse

    @staticmethod
    def git_host():
        return GitProject.git_url_parse().hostname

    @staticmethod
    def git_url():
        parse = GitProject.git_url_parse()
        return f'{parse.scheme}://{parse.hostname}'

    @staticmethod
    def git_project_url():
        parse = GitProject.git_url_parse()
        return f'{parse.scheme}://{parse.hostname}{parse.path}'

    def push_changelog(self, changelog, file_name="CHANGELOG.md"):
        data = {
            'branch': self.branch,
            'commit_message': 'changelog prepare to release',
            'actions': [
                {
                    'action': 'update',
                    'file_path': file_name,
                    'content': changelog.text()
                },
            ]
        }
        self.gitlab_project.commits.create(data)

    def _get_master_branch(self):
        return self.gitlab_project.default_branch

    def _get_git_client(self):
        return Gitlab(GitProject.git_url(), private_token=self.token)

    def _get_path_with_namespace(self):
        return self.parse.path.replace(".git", "")[1:]

    def _get_gitlab_project(self):
        return self.gitlab_client.projects.get(self.path_with_namespace)

    def _find_git_file_id(self, file_name, branch):
        result = []
        for item in self.gitlab_project.repository_tree(ref=branch):
            if item['name'] == file_name:
                return item['id']
        return result

    def get_git_file_text(self, file_name, branch):
        ci_info = self.gitlab_project.repository_blob(
            self._find_git_file_id(branch=branch, file_name=file_name), branch=branch)
        content = base64.b64decode(ci_info['content'])
        return content.decode('utf8')
