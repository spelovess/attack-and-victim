#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import json
import os
import copy
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

    # organization
    organization_response = session.get(HOST + '/adminapi/organization?type=2')
    organization_data = json.loads(organization_response.text)
    organization_id = organization_data['data'][0]['id']
    # print organization_id

    # attacker_ip
    attacker_ip_response = session.get(HOST + '/adminapi/organization-assets/attacker')
    attacker_ip_data = json.loads(attacker_ip_response.text)
    attacker_ip = attacker_ip_data['data']['list'][0]['ip']
    # print attacker_ip

    # attack_tools
    attack_tools_response = session.get(HOST + '/adminapi/attack_tools/list')
    attack_tools_data = attack_tools_response.json()
    attack_tools_ids = []
    attack_tools_ids.append(attack_tools_data['data'][0]['children'][0]['id'])
    attack_tools_ids.append(attack_tools_data['data'][1]['children'][0]['id'])
    attack_tools_ids = json.dumps(attack_tools_ids)

    threat_types_response = session.get(HOST + '/adminapi/threat_type/list')
    threat_data = threat_types_response.json()
    t = {
        'id': threat_data['data'][0]['children'][0]['id'],
        'count': 5
    }
    t2 = {
        'id': threat_data['data'][1]['children'][0]['id'],
        'count': 10
    }
    threats = [t, t2]

    # add report
    add_url = HOST + '/adminapi/report/attacker'
    add_data = {
        "victim_ip": '1.1.1.1',
        "victim_system": "system",
        "victim_url": "https://abc.com",
        "attack_type": 1,
        "attacker_ip": attacker_ip,
        "description": 'abcdefghijklmn',
        "org_dst_id": organization_id,
        "attack_tools": attack_tools_ids,
        "threats": json.dumps(threats)
    }
    pwd = os.path.dirname(os.path.abspath(__file__))
    img = open(os.path.join(pwd, "abc.jpg"), "rb")
    doc = open(os.path.join(pwd, "123.docx"), "rb")
    files = {
        "images[1]": img,
        "documents": doc,
    }

    # 错误参数情况下
    wrong_data = copy.deepcopy(add_data)
    wrong_data['attack_tools'] = '5, 7, 9'
    add_response = session.post(add_url, data=wrong_data, files=files)
    add_response_data = json.loads(add_response.text)
    if add_response.status_code == 200 and add_response_data['code'] == 1 \
            and add_response_data['info'] == u'攻击工具/威胁 类型错误':
        print '工具值传入错误，返回结果验证成功'
    else:
        print
        add_response_data['info']
        print '工具值传入错误，返回结果验证失败'
        session.close()
        return

    img.seek(0)
    doc.seek(0)

    wrong_data['attack_tools'] = '[5999, 7999, 9999]'
    add_response = session.post(add_url, data=wrong_data, files=files)
    add_response_data = json.loads(add_response.text)
    if add_response.status_code == 200 and add_response_data['code'] == 1 \
            and add_response_data['info'] == u'攻击工具不存在':
        print '工具值不存在时，返回结果验证成功'
    else:
        print
        add_response_data['info']
        print '工具值不存在时，返回结果验证失败'
        session.close()
        return

    img.seek(0)
    doc.seek(0)
    add_response = session.post(add_url, data=add_data, files=files)
    add_response_data = json.loads(add_response.text)

    if add_response.status_code == 200 and add_response_data['code'] == 0 \
            and add_response_data['info'] == u'添加成功':
        print "提交攻击队伍成绩成功"
    else:
        print "添加失败"

    session.close()


login()
