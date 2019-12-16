#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import json
import os
import config

HOST = config.host


def login():
    # login
    login_url = HOST + '/adminapi/login'
    login_data = {
        "username": "cs_victim",
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

    threat_types_response = session.get(HOST + '/adminapi/threat_type/list')
    threat_data = threat_types_response.json()
    t = {
        'id': threat_data['data'][0]['children'][1]['id'],
        'count': 5
    }
    t2 = {
        'id': threat_data['data'][1]['children'][1]['id'],
        'count': 10
    }
    threats = [t, t2]

    # add report
    add_url = HOST + '/adminapi/report/victimer'
    add_data = {
        "victim_ip": '1.1.1.1',
        "victim_system": "system",
        "victim_url": "https://abc.com",
        "attack_method": 'abc',
        "attacker_ip": '8.8.8.8',
        "description": 'abcdefghijklmn',
        "threats": json.dumps(threats)
    }
    pwd = os.path.dirname(os.path.abspath(__file__))
    img = open(os.path.join(pwd, "abc.jpg"), "rb")
    doc = open(os.path.join(pwd, "123.docx"), "rb")
    files = {
        "images[1]": img,
        "documents": doc,
    }

    add_response = session.post(add_url, data=add_data, files=files)
    add_response_data = json.loads(add_response.text)

    if add_response.status_code == 200 and add_response_data['code'] == 0 and add_response_data['info'] == u'添加成功':
        print "提交防守队伍成绩成功"
    else:
        print "添加失败"
        print
        add_response_data['info']
        return


login()
