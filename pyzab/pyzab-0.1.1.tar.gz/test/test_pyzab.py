import unittest
import os
from src.pyzab import Zabbix
from dotenv import load_dotenv

# From project directory, run:
# python -m unittest test.test_pyzab

class TestPyzab(unittest.TestCase):
    # "python -m unittest test.test_pyzab.TestPyzab.test_pz_get_host" to run a single test or
    # "python -m unittest test.test_pyzab" to run all tests
    def setUp(self): # setUp() is a method provided by unittest, which is executed before each test
        load_dotenv()
        config = {
            'zabbix_api_url': os.getenv('zabbix_url'),
            'zabbix_auth_token': os.getenv('zabbix_auth_token')
        }
        self.zabbix = Zabbix(**config)

    def test_get_host(self):
        """ Tests an API call to get info about a host."""
        host = self.zabbix.get_host(host_id="10917")
        assert isinstance(host, dict)
        assert isinstance(host['host'], str)
    
    def test_get_all_hosts(self):
        """ Tests an API call to get all hosts based on given optional filters."""
        hosts = self.zabbix.get_all_hosts(filter={"status": "1"})
        assert isinstance(hosts, list)

    def test_create_host(self):
        new_host = self.zabbix.create_host(hostname="Host para testes de API3", ip="10.99.99.99", group_id="5", template_id="10186")
        assert isinstance(new_host, dict)
        assert isinstance(new_host['hostids'], list)
        assert isinstance(new_host['hostids'][0], str)

    def test_delete_host(self):
        deleted_host = self.zabbix.delete_host(host_id="10917")
        assert isinstance(deleted_host, dict)
        assert isinstance(deleted_host['hostids'], list)
        assert deleted_host['hostids'] == '10917'

    def test_enable_host(self):
        host = self.zabbix.enable_host(host_id="10917")
        assert isinstance(host, dict)
        assert isinstance(host['hostids'], list)
        assert host['hostids'][0] == '10917'

    def test_disable_host(self):
        host = self.zabbix.disable_host(host_id="10917")
        assert isinstance(host, dict)
        assert isinstance(host['hostids'], list)
        assert host['hostids'][0] == '10917'

    def test_get_host_interface(self):
        """ Tests an API call to get all interface info of a specific host."""
        host = self.zabbix.get_host_interface(host_id="10917")
        assert isinstance(host, dict)
        assert host['hostid'] == "10917"

    def test_get_group_ids(self):
        ...

    def test_get_all_templates(self):
        ...
    


if __name__ == "__main__":
    unittest.main()