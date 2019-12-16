#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import config


def test__victimer_add_3reports():
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=config.localhost, port=config.port, username=config.user, password=config.passwd)
    # stdin,stdout,stderr=s.exec_command('/root/test.sh')
    stdin, stdout, stderr = s.exec_command('cd gongfangautotest/chengsheng;'
                                           'python 16_new_victimer_add_3report_victim_strategy_2judge.py')
    out = stdout.readlines()
    print(out)
    check = ['登陆成功\n', '提交防守队伍成绩成功\n', '登陆成功\n', '提交防守队伍成绩成功\n', '登陆成功\n', '提交防守队伍成绩成功\n']
    assert out == check
    s.close()
