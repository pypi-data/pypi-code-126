#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/6/10 10:04
# @Author : mantch
# @Version：V 1.0
# @desc : https://github.com/NLP-LOVE/Model_Log

import os
import pickle
import sqlite3
from .modellog_sqlite import ModelLogSqlite



class ModelLogWebSqlite(object):

    def __init__(self):
        self.current_path = os.path.dirname(__file__)

    # 数据库连接
    def get_conn(self):
        return sqlite3.connect(os.path.join(self.current_path, '..', 'data', 'model_log.db'))

    # 构造表头
    def generate_table_head(self, project_id):
        conn = self.get_conn()
        sql = "select sm.sub_model_id, sm.sub_model_name, sm.sub_model_remark, sm.create_time, sm.is_finish from sub_model sm where sm.project_id=%d and sm.del_flag=0" % (
            project_id)
        sub_model_result = conn.execute(sql).fetchall()

        # 构造表头
        table_head = {}
        table_length = {}
        sub_model_param = {}

        for sub_model in sub_model_result:

            sql = "select mp.param_type, mp.param_name, mp.param_value from model_param mp where mp.sub_model_id=%d" % (
                sub_model[0])
            model_param_result = conn.execute(sql)

            for model_param in model_param_result:

                # 添加 table head
                if model_param[0] not in table_head:
                    table_head[model_param[0]] = [model_param[1]]
                else:
                    if model_param[1] not in table_head[model_param[0]]:
                        table_head[model_param[0]].append(model_param[1])

                # sub_model_param
                if sub_model[0] not in sub_model_param:
                    sub_model_param[sub_model[0]] = {model_param[1]: model_param[2]}
                else:
                    sub_model_param[sub_model[0]][model_param[1]] = model_param[2]

        for type, param_list in table_head.items():
            table_length[type] = len(param_list)

        conn.close()
        return sub_model_result, sub_model_param, table_head, table_length

    # 构造页面数据
    def generate_table_data(self, table_head, sub_model_result, sub_model_param):
        conn = self.get_conn()
        table_data = []
        best_head = []
        best_data = {}
        first_param = {}
        modify_head = []
        id = 0
        for i, sub_model in enumerate(sub_model_result):

            # 评估指标数据
            sql = "select br.best_name, br.best_value from best_result br where br.sub_model_id=%d" % (sub_model[0])
            best_result = conn.execute(sql)
            dic = {}

            for best in best_result:
                if best[0] not in best_head:
                    best_head.append(best[0])

                dic[best[0]] = best[1]

            best_data[sub_model[0]] = dic

            id += 1
            dic = {}

            dic['id'] = id
            dic['sub_model_id'] = sub_model[0]
            dic['sub_model_name'] = sub_model[1]
            dic['sub_model_remark'] = sub_model[2]
            dic['create_time'] = sub_model[3]
            dic['finished_train'] = False if sub_model[4] == 0 else True

            # 超参数
            for _, param_list in table_head.items():
                for param_name in param_list:

                    try:
                        dic[param_name] = sub_model_param[sub_model[0]][param_name]
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
                    dic[name] = best_data[sub_model[0]][name]
                except:
                    dic[name] = ''

            table_data.append(dic)

        conn.close()
        return table_data, best_head, modify_head

    # 构造loss画图数据
    def generate_loss_data(self, project_id, sub_model_result):
        conn = self.get_conn()
        sql = "select max(md.epoch) from model_metric md " \
              "left join sub_model sm on sm.sub_model_id=md.sub_model_id " \
              "left join project m on m.project_id = sm.project_id " \
              "where m.project_id=%d" % (project_id)
        max_step = conn.execute(sql).fetchall()[0][0]
        x_value = [i for i in range(1, max_step + 1)]

        legend = {}
        series = []
        for i, sub_model in enumerate(sub_model_result):

            if i + 1 == len(sub_model_result):
                legend[sub_model[1] + '_train'] = 'true'
                legend[sub_model[1] + '_test'] = 'true'
            else:
                legend[sub_model[1] + '_train'] = 'false'
                legend[sub_model[1] + '_test'] = 'false'

            sql = "select md.metric_value from model_metric md where md.sub_model_id=%d and md.metric_name='train_loss'" % (
                sub_model[0])
            train_value = [value[0] for value in conn.execute(sql)]
            data_dic = {'name': sub_model[1] + '_train', 'data': str(train_value)}
            series.append(data_dic)

            sql = "select md.metric_value from model_metric md where md.sub_model_id=%d and md.metric_name='test_loss'" % (
                sub_model[0])
            test_value = [value[0] for value in conn.execute(sql)]
            data_dic = {'name': sub_model[1] + '_test', 'data': str(test_value)}
            series.append(data_dic)

        x_value = str(x_value)
        conn.close()
        return legend, x_value, series

    def generate_train_test_data(self, sub_model_result, type):
        conn = self.get_conn()

        legend = {}
        series = []
        for i, sub_model in enumerate(sub_model_result):

            if i + 1 == len(sub_model_result):
                legend[sub_model[1] + '_train'] = 'true'
                legend[sub_model[1] + '_test'] = 'true'
            else:
                legend[sub_model[1] + '_train'] = 'false'
                legend[sub_model[1] + '_test'] = 'false'

            sql = f"select md.metric_value from model_metric md where md.sub_model_id={sub_model[0]} and md.metric_name='train_{type}'"
            train_value = [value[0] for value in conn.execute(sql)]
            data_dic = {'name': sub_model[1] + '_train', 'data': str(train_value)}
            series.append(data_dic)

            sql = f"select md.metric_value from model_metric md where md.sub_model_id={sub_model[0]} and md.metric_name='test_{type}'"
            test_value = [value[0] for value in conn.execute(sql)]
            data_dic = {'name': sub_model[1] + '_test', 'data': str(test_value)}
            series.append(data_dic)

        conn.close()
        return legend, series

    def generate_new_loss(self, sub_model_id, sub_model_name, type):
        conn = self.get_conn()

        sql = f"select md.metric_value from model_metric md where md.sub_model_id={sub_model_id} and md.metric_name='train_{type}'"
        train_value = [value[0] for value in conn.execute(sql)]

        sql = f"select md.metric_value from model_metric md where md.sub_model_id={sub_model_id} and md.metric_name='test_{type}'"
        test_value = [value[0] for value in conn.execute(sql)]

        data_list_loss = {'xAxis': {'data': [i for i in range(1, len(train_value) + 1)]},
                          'series': [{'name': sub_model_name + '_train', 'data': train_value},
                                     {'name': sub_model_name + '_test', 'data': test_value}]}

        conn.close()
        return data_list_loss

    # 构造 acc画图数据
    def generate_indicater_data(self, sub_model_result, type):
        conn = self.get_conn()
        legend_acc = {}
        series_acc = []
        for i, sub_model in enumerate(sub_model_result):

            if i + 1 == len(sub_model_result):
                legend_acc[sub_model[1] + '_test'] = 'true'
            else:
                legend_acc[sub_model[1] + '_test'] = 'false'

            sql = "select md.metric_value from model_metric md where md.sub_model_id=%d and md.metric_name='%s'" % (
                sub_model[0], type)
            test_value = [value[0] for value in conn.execute(sql)]
            data_dic = {'name': sub_model[1] + '_test', 'data': str(test_value)}
            series_acc.append(data_dic)

        conn.close()
        return legend_acc, series_acc

    def generate_new_indicater_data(self, sub_model_id, sub_model_name, type):
        conn = self.get_conn()
        sql = "select md.metric_value from model_metric md where md.sub_model_id=%d and md.metric_name='%s'" % (
        sub_model_id, type)
        value_list = [value[0] for value in conn.execute(sql)]

        data_dict = {'xAxis': {'data': [i for i in range(1, len(value_list) + 1)]},
                     'series': [{'name': sub_model_name + '_test', 'data': value_list}]}

        conn.close()
        return data_dict

    # 删除model
    def delete_model(self, project_id):
        conn = self.get_conn()
        sql = "delete from project where project_id=%d" % (project_id)
        conn.execute(sql)
        conn.commit()
        conn.close()

    def delete_sub_model(self, del_set):
        conn = self.get_conn()
        sql = "delete from sub_model where sub_model_id in %s" % (del_set)
        conn.execute(sql)

        sql = "delete from model_param where sub_model_id in %s" % (del_set)
        conn.execute(sql)

        sql = "delete from model_metric where sub_model_id in %s" % (del_set)
        conn.execute(sql)

        sql = "delete from best_result where sub_model_id in %s" % (del_set)
        conn.execute(sql)

        conn.commit()
        conn.close()

    ## 模型总数
    def get_model_num(self, nick_name):
        conn = self.get_conn()
        sql = "select count(1) from sub_model sm where sm.nick_name='%s'" % (nick_name)
        model_num = conn.execute(sql).fetchall()[0][0]

        conn.close()
        return model_num


    # 进行初始化
    def init_db(self, nick_name):

        for i in ['1', '2']:
            with open(os.path.join(self.current_path, 'data', 'tf_param.pkl'), 'rb') as file:
                tf_param = pickle.load(file)
                if i == '1':
                    tf_param['learning_rate'] = 0.001

            with open(os.path.join(self.current_path, 'data', 'metric_list' + i + '.pkl'), 'rb') as file:
                metric_list = pickle.load(file)

            model_log = ModelLogSqlite(nick_name, 'demo命名实体识别')
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

            del model_log


    def get_project_num(self, nick_name):
        conn = self.get_conn()
        sql = "select count(1) as cou from project p where p.nick_name='%s'" % (nick_name)
        result = conn.execute(sql).fetchall()[0][0]

        conn.close()
        return result

    def get_project_name(self, project_id):
        conn = self.get_conn()
        sql = "select p.project_name as project_name from project p where p.project_id=%d" % (project_id)
        result = conn.execute(sql).fetchall()[0][0]

        conn.close()
        return result

    def get_max_sub_model_id(self, project_id):
        conn = self.get_conn()
        sql = "select max(sm.sub_model_id) as sub_model_id, sm.sub_model_name as sub_model_name from sub_model sm where sm.project_id=%d" % (project_id)
        result = conn.execute(sql).fetchall()[0]
        sub_model_id, sub_model_name= result[0], result[1]\

        conn.close()
        return sub_model_id, sub_model_name

    def get_max_sub_model_id_project_id(self):
        conn = self.get_conn()
        sql = "select max(sm.sub_model_id), sm.project_id from sub_model sm"
        result = conn.execute(sql).fetchall()[0][0]

        conn.close()
        return result

    def get_muti_sub_model_id_by_project_ids(self, del_set):
        conn = self.get_conn()
        sql = "select sm.sub_model_id as sub_model_id from sub_model sm where sm.project_id in %s" % (del_set)
        sub_model_list = [item[0] for item in conn.execute(sql).fetchall()]

        conn.close()
        return sub_model_list

    def get_count_best_result(self, sub_model_id):
        conn = self.get_conn()
        sql = "select count(1) as cou from best_result br where br.sub_model_id=%d" % (sub_model_id)
        result = conn.execute(sql).fetchall()[0][0]

        conn.close()
        return result

    def del_project_ids(self, del_set):
        conn = self.get_conn()
        sql = "delete from project where project_id in %s" % (del_set)
        conn.execute(sql)
        conn.commit()

        conn.close()

    def update_sub_model_finish(self, sub_model_id):
        conn = self.get_conn()
        sql = f'update sub_model set is_finish=1 where sub_model_id={sub_model_id}'
        conn.execute(sql)
        conn.commit()

        conn.close()

    def get_project_list(self, nick_name, page, page_size_1, page_size_2):
        conn = self.get_conn()
        sql = f"select m.project_name, m.project_remark, m.create_time, m.project_id from project m where " \
              f"m.del_flag = 0 and m.nick_name='{nick_name}' order by m.create_time desc limit {page_size_1},{page_size_2}"
        result = conn.execute(sql).fetchall()

        project_list = []

        id = (page - 1) * 15
        for item in result:
            id += 1
            map_ = {'id': id, 'project_name': item[0], 'project_remark': item[1], 'create_time': item[2],
                    'project_id': item[3]}
            project_list.append(map_)
        return project_list



