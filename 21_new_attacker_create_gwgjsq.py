# -*- coding: UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import config

HOST = config.host


def login():
    # login
    login_url = HOST + '/adminapi/login'
    login_data = {
        "username": "cs_attacker",
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

    # add report
    add_url = HOST + '/adminapi/high_risk/apply'
    add_data = {
        "victim_org_id": organization_id,
        "target_system": "system",
        "target_ip": '1.1.1.1',
        "target_url": "https://abc.com",
        "attack_type": 1,
        "attack_description": 'abcdefghijklmn',
    }

    add_response = session.post(add_url, data=add_data)
    add_response_data = json.loads(add_response.text)

    if add_response.status_code == 200 and add_response_data['code'] == 0 and add_response_data['info'] == u'操作成功':
        print "创建高危攻击申请成功"
    else:
        print "操作失败"

    session.close()


login()
login()
