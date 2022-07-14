import kubernetes as k
from .log import logger
import subprocess
import os
from .cap_util import (
  write,
  apply_kube,
  get_name_by_email,
  get_email_by_name,
  get_sumup_project,
  is_exist_members,
  is_project
)
from .profile import ProfileCommand
from terminaltables import AsciiTable


rb_template = """
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  annotations:
    role: edit
    user: {email}
  name: user-{kebab_email}-clusterrole-edit
  namespace: {namespace} 
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: kubeflow-edit
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: User
  name: {email}
"""

ap_template = """
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  annotations:
    role: edit
    user: {email}
  name: user-{kebab_email}-clusterrole-edit
  namespace: {namespace}
spec:
  rules:
  - when:
    - key: request.headers[kubeflow-userid]
      values:
      - {email}
"""

srb_template = """
apiVersion: rbac.istio.io/v1alpha1
kind: ServiceRoleBinding
metadata:
  annotations:
    role: edit
    user: {email}
  generation: 1
  name: user-{kebab_email}-clusterrole-edit
  namespace: {namespace}
spec:
  roleRef:
    kind: ServiceRole
    name: ns-access-istio
  subjects:
  - properties:
      request.headers[kubeflow-userid]: {email}
"""

project_template = """
apiVersion: kubeflow.org/v1beta1
kind: Profile
metadata:
  name: {namespace}
  labels:
    usage: "project"
spec:
  owner:
    kind: User
    name: {email}
"""


class ProjectCommand(object):
    """
    Manage Projects. You can create, list, join, leave, and delete projects
    """
    def ls(self):
        logger.debug("join")
        sumup = get_sumup_project()
        rows = [
            [
                x["email"],
                ",".join(x["owners"]),
                ",".join(x["members"]),
            ]
            for k, x in sumup.items()
        ]
        header = [["project_name", "owner", "members"]]
        table = AsciiTable(header + rows)
        print(table.table)

    def add(self, email, project_name):
        name = get_name_by_email(email)
        if not name:
            logger.error(f"Fail! email:'{email}' not exist.")
            return
        exist_project = get_email_by_name(project_name)
        if exist_project:
            logger.error(f"Fail! project_name:'{project_name}' already exist.")
            return
        profile = project_template.format(namespace=project_name, email=email)
        filename = f"{project_name}-profile.yaml"

        write(filename, profile)
        apply_kube(filename)
        delete_yaml(filename)


    def join(self, email, project_name):
        logger.debug("join")
        name = get_name_by_email(email)
        if not name:
            logger.error(f"Fail! email:'{email}' not exist.")
            return
        exist_project = get_email_by_name(project_name)
        if not exist_project:
            logger.error(f"Fail! project_name:'{project_name}' not exist.")
            return

        kebab_email = email.replace("@", "-").replace(".", "-")
        rb = rb_template.format(
            email=email, namespace=project_name, kebab_email=kebab_email
        )
        rb_file = f"{kebab_email}-rb.yaml"
        write(rb_file, rb)

        srb = ap_template.format(
            email=email, namespace=project_name, kebab_email=kebab_email
        )
        srb_file = f"{kebab_email}-ap.yaml"
        write(srb_file, srb)

        apply_kube(rb_file)
        apply_kube(srb_file)

    def leave(self, email, project_name):
        logger.debug("leave")
        name = get_name_by_email(email)
        if not name:
            logger.error(f"Fail! email:'{email}' not exist.")
            return
        exist_project = get_email_by_name(project_name)
        if not exist_project:
            logger.error(f"Fail! project_name:'{project_name}' not exist.")
            return

        kebab_email = email.replace("@", "-").replace(".", "-")
        name = f"user-{kebab_email}-clusterrole-edit"
        cmd = f"kubectl delete rolebinding {name} -n {project_name}"
        logger.debug(cmd)
        ret = subprocess.call(cmd, shell=True)
        logger.debug(f"kubectl result: {ret}")
        cmd = f"kubectl delete authorizationpolicy {name} -n {project_name}"
        logger.debug(cmd)
        ret = subprocess.call(cmd, shell=True)
        logger.debug(f"kubectl result: {ret}")

    def delete(self, project_name):
        logger.debug("delete")
        project = is_project(project_name)
        if not project:
            logger.error(f"Fail! project:'{project_name}' not exist.")
            return
        if is_exist_members(project_name):
            logger.error(f"Fail! project member is exist. must leave all members on project: '{project_name}'.")
            return
        ProfileCommand().delete(project_name)

def delete_yaml(filename):
    os.remove(filename)
