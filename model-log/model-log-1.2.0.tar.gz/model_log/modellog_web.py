#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/6/10 10:04
# @Author : mantch
# @Version：V 1.0
# @desc : https://github.com/NLP-LOVE/Model_Log

from flask import Flask, request, jsonify, redirect, session
from flask import render_template
import webbrowser
import argparse
import signal
import sys
import os
from .utils.modellog_web_mysql import ModelLogWebMysql
from .utils.modellog_web_sqlite import ModelLogWebSqlite

model_log_web = [ModelLogWebSqlite(), 'sqlite']

current_path = os.path.dirname(__file__)
app = Flask(__name__)
app.config["SECRET_KEY"] = "model_log"
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
page_size = 15

# 检查是否登录
def check_login(sess):

    if 'nick_name' not in session:
        return False
    elif session['nick_name'] == '':
        return False
    else:
        return True



@app.before_request
def check_platform():

    phone = ['android', 'iphone', 'ipad']

    platform = request.user_agent.platform

    try:
        platform = platform.lower()

        if platform in phone:
            return render_template('alert.html')
    except Exception as e:
        pass




@app.route('/')
def to_index():

    model_num = 0

    is_login = check_login(session)

    '''
    if is_login:
        del session['nick_name']
        is_login = False
    '''

    nick_name = ''
    if is_login:
        nick_name = session['nick_name']
        model_num = model_log_web[0].get_model_num(nick_name)

    return render_template('index.html', model_num=model_num, is_login=is_login, nick_name=nick_name, database_type=model_log_web[1])

@app.route('/login', methods=['POST'])
def login():
    nick_name = request.get_json()['nick_name']

    session['nick_name'] = nick_name
    message = {}
    message['is_success'] = True

    ## 判断是否进行初始化数据
    num = model_log_web[0].get_model_num(nick_name)

    if num == 0:
        model_log_web[0].init_db(nick_name)

    return jsonify(message)



@app.route('/project_detail')
def project_detail():

    try:
        project_id = int(request.args.get('project_id'))
    except:
        raise Exception('project id 错误!')


    # 构造表头
    sub_model_result, sub_model_param, table_head, table_length = model_log_web[0].generate_table_head(project_id)

    # 删除model
    if len(sub_model_result) == 0:
        model_log_web[0].delete_model(project_id)

        return redirect('/')

    # 构造页面数据
    table_data, best_head, modify_head = model_log_web[0].generate_table_data(table_head, sub_model_result, sub_model_param)

    # 构造loss画图数据
    legend, x_value, series = model_log_web[0].generate_loss_data(project_id, sub_model_result)

    # 构造 acc画图数据
    legend_acc, series_acc = model_log_web[0].generate_train_test_data(sub_model_result, 'acc')

    # 构造recall画图数据
    legend_recall, series_recall = model_log_web[0].generate_train_test_data(sub_model_result, 'recall')

    # 构造 precision画图数据
    legend_precision, series_precision = model_log_web[0].generate_train_test_data(sub_model_result, 'precision')

    # 构造 F1画图数据
    legend_F1, series_F1 = model_log_web[0].generate_train_test_data(sub_model_result, 'F1')

    # 模型个数
    if 'nick_name' not in session:
        return redirect('/')
    nick_name = session['nick_name']
    model_num = model_log_web[0].get_model_num(nick_name)
    sub_model_num = len(sub_model_result)

    # 是否训练完成
    is_finished_train = table_data[-1]['finished_train']

    project_name = model_log_web[0].get_project_name(project_id)

    return render_template('model_detail.html', table_head=table_head, table_data=table_data,
                           table_length=table_length, x_value=x_value, legend=legend, series=series,
                           legend_acc=legend_acc, series_acc=series_acc, best_head=best_head,
                           modify_head=modify_head, legend_precision=legend_precision,
                           series_precision=series_precision, legend_F1=legend_F1,
                           series_F1=series_F1, project_id=project_id, model_num=model_num,
                           sub_model_num=sub_model_num, is_finished_train=is_finished_train, nick_name=nick_name,
                           legend_recall=legend_recall, series_recall=series_recall, project_name=project_name)

# 动态获取最新数据
@app.route('/get_new_data', methods=['POST'])
def get_new_data():

    project_id = request.get_json()['project_id']
    message = {}


    try:


        sub_model_id, sub_model_name = model_log_web[0].get_max_sub_model_id(project_id)

        # loss
        data_list_loss = model_log_web[0].generate_new_loss(sub_model_id, sub_model_name, 'loss')

        # acc
        data_list_acc = model_log_web[0].generate_new_loss(sub_model_id, sub_model_name, 'acc')

        # recall
        data_list_recall = model_log_web[0].generate_new_loss(sub_model_id, sub_model_name, 'recall')

        # precision
        data_list_precision = model_log_web[0].generate_new_loss(sub_model_id, sub_model_name, 'precision')

        # F1
        data_list_F1 = model_log_web[0].generate_new_loss(sub_model_id, sub_model_name, 'F1')

        # 判断是否训练完成
        best_count = model_log_web[0].get_count_best_result(sub_model_id)

        if best_count == 0:
            message['finished_train'] = False
        else:
            message['finished_train'] = True

        message['is_success'] = True
        message['data'] = {'loss': data_list_loss, 'acc': data_list_acc, 'recall': data_list_recall, 'precision': data_list_precision,
                           'F1': data_list_F1}


    except Exception as e:
        message['is_success'] = False
        message['msg'] = '程序内部开小差啦！'

    return jsonify(message)


# 检测是否有模型开始训练
@app.route('/check_new_model', methods=['POST'])
def check_new_model():

    model_num = request.get_json()['model_num']
    message = {}


    try:

        nick_name = session['nick_name']
        current_model_num = model_log_web[0].get_model_num(nick_name)

        if model_num != current_model_num:
            project_id = model_log_web[0].get_max_sub_model_id_project_id()
            message['is_jump'] = True
            message['project_id'] = project_id
        else:
            message['is_jump'] = False

        message['is_success'] = True



    except:
        message['is_success'] = False
        message['msg'] = '程序内部开小差啦！'


    return jsonify(message)



# 删除model
@app.route('/del_project', methods=['POST'])
def del_model():
    del_list = request.get_json()['del_list']
    message = {}

    try:
        del_set = set()
        for id in del_list:
            del_set.add(int(id))

        del_set = str(del_set)
        del_set = del_set.replace('{', '(')
        del_set = del_set.replace('}', ')')


        sub_model_id_list = model_log_web[0].get_muti_sub_model_id_by_project_ids(del_set)
        sub_model_id_list = str(sub_model_id_list)
        sub_model_id_list = sub_model_id_list.replace('[', '(')
        sub_model_id_list = sub_model_id_list.replace(']', ')')

        model_log_web[0].delete_sub_model(sub_model_id_list)

        # 删除model
        model_log_web[0].del_project_ids(del_set)

        message['is_success'] = True


    except Exception as e:
        message['is_success'] = False
        message['msg'] = '选中id错误！'
        print(e)

    return jsonify(message)


@app.route('/del_sub_model', methods=['POST'])
def del_sub_model():

    del_list = request.get_json()['del_list']
    message = {}

    try:
        del_set = set()
        for id in del_list:
            del_set.add(int(id))

        del_set = str(del_set)
        del_set = del_set.replace('{', '(')
        del_set = del_set.replace('}', ')')

        model_log_web[0].delete_sub_model(del_set)

        message['is_success'] = True

    except Exception as e:
        message['is_success'] = False
        message['msg'] = '选中id错误！'
        print(e)


    return jsonify(message)

@app.route('/finish_model', methods=['POST'])
def finish_model():
    sub_model_id = request.get_json()['sub_model_id']
    message = {}

    try:
        model_log_web[0].update_sub_model_finish(sub_model_id)
        message['is_success'] = True

    except Exception as e:
        message['is_success'] = False
        message['msg'] = '选中id错误！'
        print(e)

    return jsonify(message)

# db operation=================================================================


# 查询项目列表
@app.route('/get_project_list')
def get_project_list():

    try:
        page = int(request.args.get('page'))
    except:
        raise Exception('页码参数错误！')

    nick_name = session['nick_name']

    project_list = model_log_web[0].get_project_list(nick_name, page, (page - 1) * page_size, page_size)

    return jsonify(project_list)

# 查询项目总页数
@app.route('/get_page_num')
def get_page_num():

    if not check_login(session):
        return '-1'


    result = model_log_web[0].get_project_num(session['nick_name'])

    page_num = result / page_size

    if int(page_num) < page_num:
        page_num = int(page_num) + 1
    else:
        page_num = int(page_num)

    return str(page_num)

@app.route('/alert')
def alert():
    return render_template('alert.html')

# 切换数据库
@app.route('/switchdatabase', methods=['POST'])
def switchdatabase():

    params = request.get_json()
    message = {}
    message['is_success'] = 'true'

    # 判断是否是mysql
    if params['database_type'] == 'sqlite':
        model_log_web[0] = ModelLogWebSqlite()
        model_log_web[1] = 'sqlite'
    else:
        try:
            model_log_web[0] = ModelLogWebMysql(params['host'], int(params['port']), params['username'], params['password'], params['database'], session['nick_name'])
            model_log_web[1] = 'mysql'
        except Exception as e:
            message['is_success'] = 'false'

    return jsonify(message)



def my_exit(signum, frame):
    print()
    print('Good By!')
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, my_exit)
    signal.signal(signal.SIGTERM, my_exit)

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", type=int, default=5432, help="指定端口号")
    args = parser.parse_args()

    try:
        webbrowser.open('http://127.0.0.1:%d/' % (args.p))
        app.run(host='0.0.0.0', port=args.p, debug=True)
    except Exception as e:
        print(str(args.p) + '端口已占用，请使用 model-log -p=5000 指定端口号，或关闭' + str(args.p) + '端口!')


if __name__ == '__main__':
    main()


