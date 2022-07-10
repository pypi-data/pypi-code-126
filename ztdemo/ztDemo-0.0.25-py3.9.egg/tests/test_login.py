# -*-coding=utf-8 -*-

from assertpy import assert_that
from ztDemo.common.data_processor import data_provider
from ztDemo.common.my_logger import MyLogger
from ztDemo.common.test_decorator import Test
from ztDemo.my_pages.login_page import LoginAPI, LoginPage
from ztDemo.settings.global_config import get_config


log = MyLogger(file_name='debug_info.log').get_logger(__name__)


class ZenTaoTest:
    test_case_id = 'Jira-1025'

    @data_provider([('itesting', 'P@ssw0rd', '测试账户')])
    # 给测试方法添加tag标签，指定其tag值为smoke
    @Test(tag='API')
    def test_login(self, *test_data):
        env = get_config('config')
        login_page = LoginAPI(env["DOMAIN"])
        user_name, password, accounts_name = test_data
        log.info("用户名是{0}, 密码是{1}, 账户登录态是{2}".format(user_name, password, accounts_name))
        result = login_page.login(user_name, password)
        assert_that(result.status_code).is_equal_to(200)
        assert_that(result.text).contains(accounts_name)
        assert_that(result.text).contains("退出")

    @data_provider([('itesting', 'P@ssw0rd', '测试账户')])
    @Test(tag='UI')
    def test_ui_login(self, *test_data):
        env = get_config('config')
        login_page = LoginPage('chrome', env["DOMAIN"])
        user_name, password, accounts_name = test_data
        log.info("用户名是{0}, 密码是{1}, 账户登录态是{2}".format(user_name, password, accounts_name))
        login_page.login(user_name, password)
