# -*- coding: UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import time
import config

HOST = config.host


def login1():
    # login
    login_url = HOST + '/adminapi/login'
    login_data = {
        "username": "cs_judge1",
        "password": "0192023a7bbd73250516f069df18b500",  # admin123
        "captcha": "abc"
    }

    headers = {'content-type': 'application/json'}
    session = requests.Session()
    login_response = session.post(login_url, data=json.dumps(login_data), headers=headers)
    login_data = json.loads(login_response.text)
    if login_response.status_code == 200 and login_data['code'] == 0:
        print "登陆成功"
    else:
        print "登陆失败"
        return

    # 攻击队伍
    organization_response = session.get(HOST + '/adminapi/organization?type=1')
    organization_data = json.loads(organization_response.text)
    organization_id = organization_data['data'][0]['id']
    # print organization_id

    # 新增攻击方违规行为扣分
    add_url = HOST + '/adminapi/create-dispose'
    add_data = {
        "org_id": organization_id,
        "happen_time": '2019-11-08 16:50:09',
        "description": "asdfasf",
        "score": 222,
        "type": 1,
    }

    add_response = session.post(add_url, data=add_data)
    add_response_data = json.loads(add_response.text)

    if add_response.status_code == 200 and add_response_data['code'] == 0 \
            and add_response_data['info'] == u'添加处置成功':
        print "添加攻击队违规行为处置成功"
    else:
        print "添加处置失败"

    session.close()


def login2():
    # login
    login_url = HOST + '/adminapi/login'
    login_data = {
        "username": "cs_judge1",
        "password": "0192023a7bbd73250516f069df18b500",  # admin123
        "captcha": "abc"
    }

    headers = {'content-type': 'application/json'}
    session = requests.Session()
    login_response = session.post(login_url, data=json.dumps(login_data), headers=headers)
    login_data = json.loads(login_response.text)
    if login_response.status_code == 200 and login_data['code'] == 0:
        print "登陆成功"
    else:
        print "登陆失败"
        return

    # 防守队伍
    organization_response = session.get(HOST + '/adminapi/organization?type=2')
    organization_data = json.loads(organization_response.text)
    organization_id = organization_data['data'][0]['id']
    # print organization_id

    # 新增攻击方违规行为扣分
    add_url = HOST + '/adminapi/create-dispose'
    add_data = {
        "org_id": organization_id,
        "happen_time": '2019-11-08 16:50:09',
        "description": "asdfasf",
        "score": 222,
        "type": 2,
    }

    add_response = session.post(add_url, data=add_data)
    add_response_data = json.loads(add_response.text)

    if add_response.status_code == 200 and add_response_data['code'] == 0 \
            and add_response_data['info'] == u'添加处置成功':
        print "添加防守队违规行为处置成功"
    else:
        print "添加处置失败"

    session.close()


login1()
time.sleep(1)
login2()
