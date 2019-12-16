#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import config


def test_attacker_create_gwgjsq():
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=config.localhost, port=config.port, username=config.user, password=config.passwd)
    # stdin,stdout,stderr=s.exec_command('/root/test.sh')
    stdin, stdout, stderr = s.exec_command('cd gongfangautotest/chengsheng;'
                                           'python 21_new_attacker_create_gwgjsq.py')
    out = stdout.readlines()
    print(out)
    check = ['登陆成功\n', '创建高危攻击申请成功\n', '登陆成功\n', '创建高危攻击申请成功\n']
    assert out == check
    s.close()
