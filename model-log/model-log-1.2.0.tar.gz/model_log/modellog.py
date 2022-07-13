#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/6/10 10:04
# @UpdateTime: 2022/7/12 20:17
# @Author : mantch
# @Version：V 2.0
# @desc : https://github.com/NLP-LOVE/Model_Log

import os
from .utils.modellog_mysql import ModelLogMysql
from .utils.modellog_sqlite import ModelLogSqlite
current_path = os.path.dirname(__file__)


class ModelLog(object):

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
    def __init__(self, nick_name, project_name, project_remark='', db_host=None, db_port=None, db_username=None, db_password=None, data_base=None):

        if db_host is None:
            self.model_log = ModelLogSqlite(nick_name, project_name, project_remark)
            self.db_type = 'sqlite'
        else:
            self.model_log = ModelLogMysql(nick_name, project_name, db_host, db_port, db_username, db_password, data_base, project_remark)
            self.db_type = 'mysql'



    # 检查project name 是否存在
    def __is_exist_project_name(self, project_name):
        return self.model_log.is_exist_project_name(project_name)

    # 检查model name 是否存在
    def __is_exist_model_name(self, model_name, project_id):
        return self.model_log.is_exist_project_name(model_name, project_id)


    """
    :param param_dict: dict，训练参数字典
    :param param_type: str，参数类型，例如：TF参数、word2vec参数等。
    """
    def add_param(self, param_dict, param_type):
        self.model_log.add_param(param_dict, param_type)

    """
    :param model_name: str，模型名称
    """
    def add_model_name(self, model_name):
        self.model_log.add_model_name(model_name)

    """
    :param remark: str，模型备注
    """
    def add_model_remark(self, remark):
        self.model_log.add_model_remark(remark)


    """
    :param metric_name:  str，评估指标名称，可选择['train_loss', 'test_loss', 'test_acc', 'test_recall', 'test_precision', 'test_F1']
    :param metric_value: float，评估指标数值。
    :param epoch:        int，训练周期

    第一次调用该 API 时，会把以上设置的数据持久化到 SQLite 数据库。
    可以在每个 epoch 周期的最后使用该 API添加训练集和测试集的评估指标，web端会自动获取该数据。
    """
    def add_metric(self, metric_name, metric_value, epoch):
        self.model_log.add_metric(metric_name, metric_value, epoch)


    """
    :param best_name:  str，最佳评估指标名称，
    :param best_value: float，最佳评估指标数值。
    :param best_epoch: int，训练周期

    添加当前模型训练中最佳的评估数据，一般放到模型训练的最后进行添加。
    """
    def add_best_result(self, best_name, best_value, best_epoch):
        self.add_best_result(best_name, best_value, best_epoch)

    def finish_model(self):
        self.model_log.finish_model()


    # 检查model_name是否重复
    def __check_model_name(self, model_name, sub_model_count, project_id):
        return self.model_log.check_model_name(model_name, sub_model_count, project_id)


    # 添加模型数据
    def __add_model_data(self):
        self.model_log.add_model_data()

    # db数据库初始化
    def __init_db(self):
        self.model_log.init_db()

    """
    关闭 SQLite 数据库连接
    """
    def close(self):
        if self.db_type == 'sqlite':
            self.model_log.close()


if __name__ == '__main__':

    model_log = ModelLog('test项目', 'test备注')
    batch_size = 6
    lr = 2e-5
    epock = 100
    num_hiddens = 768
    ffn_num_hiddens = num_hiddens
    ffn_num_input = num_hiddens
    num_heads, max_len = 12, 512
    num_layers, dropout = 12, 0.1

    model_log.add_model_name(model_name='s')
    model_log.add_model_remark(remark='1')
    model_log.add_param(param_dict={'lr': lr, 'num_hiddens': num_hiddens, 'batch_size': batch_size,
                                    'num_heads': num_heads, 'num_layers': num_layers, 'dropout': dropout},
                        param_type='torch_param')

    model_log.add_metric(metric_name='train_loss', metric_value=1, epoch=1)
    model_log.add_metric(metric_name='train_acc', metric_value=1, epoch=1)
    model_log.add_metric(metric_name='test_acc', metric_value=1, epoch=1)
    print()








