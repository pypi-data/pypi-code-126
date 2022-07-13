#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/6/10 10:04
# @Author : mantch
# @Version：V 1.0
# @desc : https://github.com/NLP-LOVE/Model_Log

import os
import pickle
from .modellog_mysql import ModelLogMysql
from .mysql_utils import MySQLDao





class ModelLogWebMysql(object):

    def __init__(self, db_host, db_port, db_username, db_password, data_base, nick_name):
        self.dao = MySQLDao(db_host, db_port, db_username, db_password, data_base)
        self.current_path = os.path.dirname(__file__)

        # 判断是否进行初始化
        sql = "SHOW TABLES LIKE 'project'"
        result = self.dao.query(sql)
        if len(result) == 0:
            self.init_db(nick_name)

    # 构造表头
    def generate_table_head(self, project_id):
        sql = f'select sm.sub_model_id, sm.sub_model_name, sm.sub_model_remark, sm.create_time, sm.is_finish from sub_model sm where sm.project_id={project_id} and sm.del_flag=0'
        sub_model_result = self.dao.query(sql)

        # 构造表头
        table_head = {}
        table_length = {}
        sub_model_param = {}

        for sub_model in sub_model_result:

            sql = f'select mp.param_type, mp.param_name, mp.param_value from model_param mp where mp.sub_model_id={sub_model["sub_model_id"]}'
            model_param_result = self.dao.query(sql)

            for model_param in model_param_result:

                # 添加 table head
                if model_param['param_type'] not in table_head:
                    table_head[model_param['param_type']] = [model_param['param_name']]
                else:
                    if model_param['param_name'] not in table_head[model_param['param_type']]:
                        table_head[model_param['param_type']].append(model_param['param_name'])

                # sub_model_param
                if sub_model['sub_model_id'] not in sub_model_param:
                    sub_model_param[sub_model['sub_model_id']] = {model_param['param_name']: model_param['param_value']}
                else:
                    sub_model_param[sub_model['sub_model_id']][model_param['param_name']] = model_param['param_value']

        for type, param_list in table_head.items():
            table_length[type] = len(param_list)


        return sub_model_result, sub_model_param, table_head, table_length



    # 构造页面数据
    def generate_table_data(self, table_head, sub_model_result, sub_model_param):
        table_data = []
        best_head = []
        best_data = {}
        first_param = {}
        modify_head = []
        id = 0
        for i, sub_model in enumerate(sub_model_result):

            # 评估指标数据
            sql = f'select br.best_name, br.best_value from best_result br where br.sub_model_id={sub_model["sub_model_id"]}'
            best_result = self.dao.query(sql)
            dic = {}

            for best in best_result:
                if best['best_name'] not in best_head:
                    best_head.append(best['best_name'])

                dic[best['best_name']] = best['best_value']

            best_data[sub_model['sub_model_id']] = dic

            id += 1
            dic = {}

            dic['id'] = id
            dic['sub_model_id'] = sub_model['sub_model_id']
            dic['sub_model_name'] = sub_model['sub_model_name']
            dic['sub_model_remark'] = sub_model['sub_model_remark']
            dic['create_time'] = sub_model['create_time']
            dic['finished_train'] = False if sub_model['is_finish'] == 0 else True

            # 超参数
            for _, param_list in table_head.items():
                for param_name in param_list:

                    try:
                        dic[param_name] = sub_model_param[sub_model['sub_model_id']][param_name]
                    except:
                        dic[param_name] = ''

                    if i == 0:  # 记录第一次训练的超参数
                        first_param[param_name] = dic[param_name]
                    else:
                        if dic[param_name] != first_param[param_name]:
                            modify_head.append(param_name)

            # 评估指标数据
            for name in best_head:
                try:
                    dic[name] = best_data[sub_model['sub_model_id']][name]
                except:
                    dic[name] = ''

            table_data.append(dic)


        return table_data, best_head, modify_head


    # 构造loss画图数据
    def generate_loss_data(self, project_id, sub_model_result):
        sql = "select max(md.epoch) as max_step from model_metric md " \
              "left join sub_model sm on sm.sub_model_id=md.sub_model_id " \
              "left join project m on m.project_id = sm.project_id " \
              f"where m.project_id={project_id}"
        max_step = self.dao.query(sql)[0]['max_step']
        x_value = [i for i in range(1, max_step + 1)]

        legend = {}
        series = []
        for i, sub_model in enumerate(sub_model_result):

            if i + 1 == len(sub_model_result):
                legend[sub_model['sub_model_name'] + '_train'] = 'true'
                legend[sub_model['sub_model_name'] + '_test'] = 'true'
            else:
                legend[sub_model['sub_model_name'] + '_train'] = 'false'
                legend[sub_model['sub_model_name'] + '_test'] = 'false'

            sql = f"select md.metric_value as metric_value from model_metric md where md.sub_model_id={sub_model['sub_model_id']} and md.metric_name='train_loss'"
            train_value = [value['metric_value'] for value in self.dao.query(sql)]
            data_dic = {'name': sub_model['sub_model_name'] + '_train', 'data': str(train_value)}
            series.append(data_dic)

            sql = f"select md.metric_value as metric_value from model_metric md where md.sub_model_id={sub_model['sub_model_id']} and md.metric_name='test_loss'"
            test_value = [value['metric_value'] for value in self.dao.query(sql)]
            data_dic = {'name': sub_model['sub_model_name'] + '_test', 'data': str(test_value)}
            series.append(data_dic)

        x_value = str(x_value)

        return legend, x_value, series


    def generate_train_test_data(self, sub_model_result, type):

        legend = {}
        series = []
        for i, sub_model in enumerate(sub_model_result):

            if i + 1 == len(sub_model_result):
                legend[sub_model['sub_model_name'] + '_train'] = 'true'
                legend[sub_model['sub_model_name'] + '_test'] = 'true'
            else:
                legend[sub_model['sub_model_name'] + '_train'] = 'false'
                legend[sub_model['sub_model_name'] + '_test'] = 'false'

            sql = f"select md.metric_value as metric_value from model_metric md where md.sub_model_id={sub_model['sub_model_id']} and md.metric_name='train_{type}'"
            train_value = [value['metric_value'] for value in self.dao.query(sql)]
            data_dic = {'name': sub_model['sub_model_name'] + '_train', 'data': str(train_value)}
            series.append(data_dic)

            sql = f"select md.metric_value as metric_value from model_metric md where md.sub_model_id={sub_model['sub_model_id']} and md.metric_name='test_{type}'"
            test_value = [value['metric_value'] for value in self.dao.query(sql)]
            data_dic = {'name': sub_model['sub_model_name'] + '_test', 'data': str(test_value)}
            series.append(data_dic)

        return legend, series

    def generate_new_loss(self, sub_model_id, sub_model_name, type):

        sql = f"select md.metric_value as metric_value from model_metric md where md.sub_model_id={sub_model_id} and md.metric_name='train_{type}'"
        train_value = [value['metric_value'] for value in self.dao.query(sql)]

        sql = f"select md.metric_value as metric_value from model_metric md where md.sub_model_id={sub_model_id} and md.metric_name='test_{type}'"
        test_value = [value['metric_value'] for value in self.dao.query(sql)]

        data_list_loss = {'xAxis':{'data':[i for i in range(1, len(train_value) + 1)]},
                          'series':[{'name':sub_model_name + '_train', 'data':train_value},
                                    {'name':sub_model_name + '_test', 'data':test_value}]}

        return data_list_loss


    # 构造 acc画图数据
    def generate_indicater_data(self, sub_model_result, type):
        legend_acc = {}
        series_acc = []
        for i, sub_model in enumerate(sub_model_result):

            if i + 1 == len(sub_model_result):
                legend_acc[sub_model['sub_model_name'] + '_test'] = 'true'
            else:
                legend_acc[sub_model['sub_model_name'] + '_test'] = 'false'

            sql = f'select md.metric_value as metric_value from model_metric md where md.sub_model_id={sub_model["sub_model_id"]} and md.metric_name="{type}"'
            test_value = [value['metric_value'] for value in self.dao.query(sql)]
            data_dic = {'name': sub_model[1] + '_test', 'data': str(test_value)}
            series_acc.append(data_dic)

        return legend_acc, series_acc

    def generate_new_indicater_data(self, sub_model_id, sub_model_name, type):

        sql = f'select md.metric_value as metric_value from model_metric md where md.sub_model_id={sub_model_id} and md.metric_name="{type}"'
        value_list = [value['metric_value'] for value in self.dao.query(sql)]

        data_dict = {'xAxis': {'data': [i for i in range(1, len(value_list) + 1)]},
                          'series': [{'name': sub_model_name + '_test', 'data': value_list}]}

        return data_dict

    # 删除model
    def delete_model(self, project_id):
        sql = f"delete from project where project_id={project_id}"
        self.dao.execute(sql)


    def delete_sub_model(self, del_set):
        sql = f"delete from sub_model where sub_model_id in %s" % (del_set)
        self.dao.execute(sql)

        sql = "delete from model_param where sub_model_id in %s" % (del_set)
        self.dao.execute(sql)

        sql = "delete from model_metric where sub_model_id in %s" % (del_set)
        self.dao.execute(sql)

        sql = "delete from best_result where sub_model_id in %s" % (del_set)
        self.dao.execute(sql)


    ## 模型总数
    def get_model_num(self, nick_name):
        sql = f'select count(1) as cou from sub_model sm where sm.nick_name="{nick_name}"'
        model_num = self.dao.query(sql)[0]['cou']
        return model_num

    # 进行初始化
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

            model_log = ModelLogMysql(nick_name, 'demo命名实体识别', db_host=self.dao.db_host, db_port=self.dao.db_port,
                                 db_username=self.dao.db_username, db_password=self.dao.db_password, data_base=self.dao.data_base)
            model_log.add_model_name('BILSTM_CRF模型')
            model_log.add_param(tf_param, 'tf_param')

            for n, item in enumerate(metric_list):
                model_log.add_metric('train_loss', item['train_loss'], n + 1)
                model_log.add_metric('test_loss', item['test_loss'], n + 1)
                model_log.add_metric('test_acc', item['test_acc'], n + 1)
                model_log.add_metric('test_recall', item['test_recall'], n + 1)
                model_log.add_metric('test_precision', item['test_precision'], n + 1)
                model_log.add_metric('test_F1', item['test_F1'], n + 1)

            if i == '1':
                model_log.add_best_result('best_loss', 4.9491, 14)
                model_log.add_best_result('best_acc', 0.8937, 14)
                model_log.add_best_result('best_precision', 0.8315, 14)
                model_log.add_best_result('best_F1', 0.8615, 14)
                model_log.add_best_result('best_step', 14, 14)
            else:
                model_log.add_best_result('best_loss', 2.7031, 29)
                model_log.add_best_result('best_acc', 0.8937, 29)
                model_log.add_best_result('best_precision', 0.8285, 29)
                model_log.add_best_result('best_F1', 0.8598, 29)
                model_log.add_best_result('best_step', 29, 29)

            model_log.finish_model()
            del model_log

    def get_project_num(self, nick_name):
        sql = "select count(1) as cou from project p where p.nick_name='%s'" % (nick_name)
        return self.dao.query(sql)[0]['cou']

    def get_project_name(self, project_id):
        sql = "select p.project_name as project_name from project p where p.project_id=%d" % (project_id)
        return self.dao.query(sql)[0]['project_name']

    def get_max_sub_model_id(self, project_id):
        sql = "select sm.sub_model_id as sub_model_id, sm.sub_model_name as sub_model_name from sub_model sm where sm.project_id=%d order by sm.sub_model_id desc limit 1" % (project_id)
        result = self.dao.query(sql)
        return result[0]['sub_model_id'], result[0]['sub_model_name']

    def get_max_sub_model_id_project_id(self):
        sql = "select sm.sub_model_id, sm.project_id from sub_model sm order by sm.sub_model_id desc limit 1"
        return self.dao.query(sql)[0]['project_id']

    def get_muti_sub_model_id_by_project_ids(self, del_set):
        sql = "select sm.sub_model_id as sub_model_id from sub_model sm where sm.project_id in %s" % (del_set)
        return [item['sub_model_id'] for item in self.dao.query(sql)]

    def get_count_best_result(self, sub_model_id):
        sql = "select count(1) as cou from best_result br where br.sub_model_id=%d" % (sub_model_id)
        return self.dao.query(sql)[0]['cou']

    def del_project_ids(self, del_set):
        sql = "delete from project where project_id in %s" % (del_set)
        self.dao.execute(sql)

    def update_sub_model_finish(self, sub_model_id):
        sql = f'update sub_model set is_finish=1 where sub_model_id={sub_model_id}'
        self.dao.execute(sql)

    def get_project_list(self, nick_name, page, page_size_1, page_size_2):
        sql = f"select m.project_name as project_name, m.project_remark as project_remark, m.create_time as create_time, " \
              f"m.project_id as project_id from project m where " \
              f"m.del_flag = 0 and m.nick_name='{nick_name}' order by m.create_time desc limit {page_size_1},{page_size_2}"
        result = self.dao.query(sql)

        project_list = []

        id = (page - 1) * 15
        for item in result:
            id += 1
            map_ = {'id': id, 'project_name': item['project_name'], 'project_remark': item['project_remark'], 'create_time': item['create_time'],
                    'project_id': item['project_id']}
            project_list.append(map_)
        return project_list



