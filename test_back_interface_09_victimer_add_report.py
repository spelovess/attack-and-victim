#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import config


def test_add_victim_report():
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=config.localhost, port=config.port, username=config.user, password=config.passwd)
    # stdin,stdout,stderr=s.exec_command('/root/test.sh')
    stdin, stdout, stderr = s.exec_command('cd gongfangautotest/chengsheng;'
                                           'python 09_new_admin_add_report_victim_strategy_1judge.py')
    out = stdout.readlines()
    print(out)
    check = ['登陆成功\n', '提交防守队伍成绩成功\n']
    assert out == check
    s.close()
