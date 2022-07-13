#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/6/10 10:04
# @UpdateTime: 2022/7/12 20:17
# @Author : mantch
# @Version：V 2.0
# @desc : https://github.com/NLP-LOVE/Model_Log

import time
import os
from .mysql_utils import MySQLDao
import pickle


def check_str(s, type):
    if not isinstance(s, str):
        raise Exception(type + ' not string!')
    elif s == '':
        raise Exception(type + ' is null!')


class ModelLogMysql(object):
    """
    :param nick_name:        str，昵称，多人使用下可起到数据隔离。
    :param project_name:     str，项目名称。
    :param project_remark:   str，项目备注，默认为空。
    :param db_host:          str, 可选项，可填写 Mysql 数据库ip，数据保存到数据库中，如不填，默认使用本地sqlite数据库
    :param db_port:          str | int, 可选项
    :param db_username:      str, 可选项
    :param db_password       str, 可选项
    :param data_base           str, 可选项  需要连接的数据库名

    项目名称如不存在会新建
    """

    def __init__(self, nick_name, project_name, db_host, db_port, db_username, db_password, data_base, project_remark=''):

        self.current_path = os.path.dirname(__file__)
        self.db_type = 'mysql'
        self.dao = MySQLDao(db_host, int(db_port), db_username, db_password, data_base)

        # 判断是否需要初始化
        sql = "SHOW TABLES LIKE 'project'"
        result = self.dao.query(sql)
        if len(result) == 0:
            self.init_db(nick_name)

        self.nick_name = nick_name
        self.project_name = project_name
        self.project_remark = project_remark
        self.start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.is_add_model_data = True
        self.param_dict = {}
        self.model_name = ''
        self.remark = ''

        check_str(project_name, 'project_name')
        check_str(nick_name, 'nick_name')

    # 检查project name 是否存在
    def is_exist_project_name(self, project_name):

        sql = "select 1 from project m where m.project_name = '%s' and m.nick_name='%s'" % (
        project_name, self.nick_name)
        project_table = self.dao.query(sql)

        if len(project_table) != 0:
            return True
        else:
            return False

    # 检查model name 是否存在
    def is_exist_model_name(self, model_name, project_id):

        sql = "select 1 from sub_model  sm where sm.project_id = %d and sm.sub_model_name = '%s'" % (
        project_id, model_name)
        project_table = self.dao.query(sql)

        if len(project_table) != 0:
            return True
        else:
            return False

    """
    :param param_dict: dict，训练参数字典
    :param param_type: str，参数类型，例如：TF参数、word2vec参数等。
    """

    def add_param(self, param_dict, param_type):

        check_str(param_type, 'param_type')

        self.param_dict[param_type] = param_dict

    """
    :param model_name: str，模型名称
    """

    def add_model_name(self, model_name):

        check_str(model_name, 'model_name')

        self.model_name = model_name

    """
    :param remark: str，模型备注
    """

    def add_model_remark(self, remark):

        check_str(remark, 'remark')

        self.remark = remark

    """
    :param metric_name:  str，评估指标名称，可选择['train_loss', 'test_loss', 'test_acc', 'test_recall', 'test_precision', 'test_F1']
    :param metric_value: float，评估指标数值。
    :param epoch:        int，训练周期

    第一次调用该 API 时，会把以上设置的数据持久化到 SQLite 数据库。
    可以在每个 epoch 周期的最后使用该 API添加训练集和测试集的评估指标，web端会自动获取该数据。
    """

    def add_metric(self, metric_name, metric_value, epoch):

        check_str(metric_name, 'metric_name')

        if metric_name not in ['train_loss', 'test_loss', 'train_acc', 'test_acc', 'train_recall', 'test_recall',
                               'train_precision', 'test_precision', 'train_F1', 'test_F1']:
            raise Exception(
                "Your metric_name：%s, not in ['train_loss', 'test_loss', 'test_acc', 'test_recall', 'test_precision', 'test_F1']" % (
                    metric_name))

        if self.is_add_model_data:
            self.add_model_data()
            self.is_add_model_data = False

        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sql = f'insert into model_metric values (null, {self.sub_model_id}, "{metric_name}", "line", {epoch}, {round(metric_value, 4)}, "{create_time}")'
        self.dao.execute(sql)

    """
    :param best_name:  str，最佳评估指标名称，
    :param best_value: float，最佳评估指标数值。
    :param best_epoch: int，训练周期

    添加当前模型训练中最佳的评估数据，一般放到模型训练的最后进行添加。
    """

    def add_best_result(self, best_name, best_value, best_epoch):

        check_str(best_name, 'best_name')

        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sql = f'insert into best_result values (null, {self.sub_model_id}, "{best_name}", {round(best_value, 4)}, {best_epoch}, "{create_time}")'
        self.dao.execute(sql)

    def finish_model(self):
        sql = f"update sub_model set is_finish=1 where sub_model_id={self.sub_model_id}"
        self.dao.execute(sql)

    # 检查model_name是否重复
    def check_model_name(self, model_name, sub_model_count, project_id):

        if model_name == '':
            model_name = self.project_name + '_' + str(sub_model_count + 1)

        else:

            # 判断是否有model_name
            if self.is_exist_model_name(model_name, project_id):
                model_name = model_name + '_' + str(sub_model_count + 1)
            else:
                model_name = self.model_name

        if self.is_exist_model_name(model_name, project_id):
            return self.check_model_name(model_name, sub_model_count, project_id)
        else:
            return model_name

    # 添加模型数据
    def add_model_data(self):

        # 插入model
        if not self.is_exist_project_name(self.project_name):
            sql = f'insert into project values (null, "{self.project_name}", "{self.project_remark}", "{self.nick_name}", "{self.start_time}", 0)'
            self.dao.execute(sql)

        sql = f'select project_id from project m where m.project_name = "{self.project_name}" and m.nick_name="{self.nick_name}"'
        project_id = self.dao.query(sql)[0]['project_id']

        sql = f'select count(1) as cou from sub_model sm where sm.project_id = {project_id}'
        sub_model_count = self.dao.query(sql)[0]['cou']

        # 插入sub model
        model_name = self.check_model_name(self.model_name, sub_model_count, project_id)
        sql = f'insert into sub_model values (null, {project_id}, {sub_model_count + 1}, "{model_name}", "{self.remark}", "{self.nick_name}", "{self.start_time}", 0, 0)'
        self.dao.execute(sql)

        sql = f'select sub_model_id from sub_model sm where sm.project_id = {project_id} and sm.sub_model_name = "{model_name}"'
        self.sub_model_id = self.dao.query(sql)[0]['sub_model_id']

        # 插入model param
        for param_type, value in self.param_dict.items():

            for param_name, param_value in value.items():
                sql = f'insert into model_param values (null, {self.sub_model_id}, "{param_type}", "{param_name}", "{str(param_value)}", "{self.start_time}")'
                self.dao.execute(sql)

    # db数据库初始化
    def init_db(self, nick_name):

        sql_script = open(os.path.join(self.current_path, '..', 'data', 'init_mysql.sql'), 'r', encoding='utf-8').read()
        for sql in sql_script.split(';'):
            sql = sql.replace('\n', ' ').replace('\t', ' ')
            if sql != '':
                self.dao.execute(sql)


        for i in ['1','2']:
            with open(os.path.join(self.current_path, '..', 'data', 'tf_param.pkl'), 'rb') as file:
                tf_param = pickle.load(file)
                if i == '1':
                    tf_param['learning_rate'] = 0.001

            with open(os.path.join(self.current_path, '..', 'data', 'metric_list' + i + '.pkl'), 'rb') as file:
                metric_list = pickle.load(file)

            self.nick_name = nick_name
            self.project_name = 'demo命名实体识别'
            self.project_remark = ''
            self.start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.is_add_model_data = True
            self.param_dict = {}
            self.model_name = ''
            self.remark = ''

            self.add_model_name('BILSTM_CRF模型')
            self.add_param(tf_param, 'tf_param')

            for n, item in enumerate(metric_list):
                self.add_metric('train_loss', item['train_loss'], n + 1)
                self.add_metric('test_loss', item['test_loss'], n + 1)
                self.add_metric('test_acc', item['test_acc'], n + 1)
                self.add_metric('test_recall', item['test_recall'], n + 1)
                self.add_metric('test_precision', item['test_precision'], n + 1)
                self.add_metric('test_F1', item['test_F1'], n + 1)

            if i == '1':
                self.add_best_result('best_loss', 4.9491, 14)
                self.add_best_result('best_acc', 0.8937, 14)
                self.add_best_result('best_precision', 0.8315, 14)
                self.add_best_result('best_F1', 0.8615, 14)
                self.add_best_result('best_step', 14, 14)
            else:
                self.add_best_result('best_loss', 2.7031, 29)
                self.add_best_result('best_acc', 0.8937, 29)
                self.add_best_result('best_precision', 0.8285, 29)
                self.add_best_result('best_F1', 0.8598, 29)
                self.add_best_result('best_step', 29, 29)



