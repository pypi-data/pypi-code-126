from utils import copy_merge_recursive_dict
from test_case import TestCase
import re
import yaml
import os

class TestCaseLoader():
    def __init__(self, global_config):
        self.test_case_config = global_config.get_node('testcase')
        self.test_cases_files = self.test_case_config.get_node('test_cases_files')
        self.test_case_base_path = self.test_case_config.get('base_path')
        self.common_conf = {}
        self.test_cases = []
        re_filtre = re.compile("^{}$".format(global_config.get('testcase::filtre_regex')))
        # Chargement des configs communes
        if self.test_cases_files.exist('common_config'):
            for cf_path in self.test_cases_files.get_node('common_config').config:
                common_config = yaml.load(open('{}/{}'.format(self.test_case_base_path, cf_path)), Loader=yaml.Loader)

                # Les configs sont merges sucessivements dans l'ordre
                self.common_conf = copy_merge_recursive_dict(
                    defaut=self.common_conf,
                    source=common_config
                )
        list_test_case = []
        for root, dirs, files in os.walk(self.test_case_base_path):
            for file in files:
                if file.endswith(".yaml") and file.startswith('testauto_'):
                     relpath = os.path.join(root, file).replace(self.test_case_base_path+'/', '')
                     list_test_case.append(relpath)

        # Chargement des tests cases
        for tc_path in list_test_case:
            test_case = yaml.load(open('{}/{}'.format(self.test_case_base_path, tc_path)), Loader=yaml.Loader)
            tc_name = tc_path.replace('/', '.').replace('.yml', '').replace('.yaml', '')
            if re_filtre.match(tc_name):
                # Les configs sont merges sucessivements avec la config global
                self.test_cases.append(
                    # TODO check testcase classname dans conf
                    TestCase(
                        global_config=global_config,
                        config_path=tc_path,
                        name=tc_name,
                        test_case_conf=copy_merge_recursive_dict(
                            defaut=self.common_conf,
                            source=test_case
                        )
                    )
                )

    def get_test_cases(self):
        return self.test_cases
