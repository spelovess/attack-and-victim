#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import config


def test_judge_create_wgxwkf():
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=config.localhost, port=config.port, username=config.user, password=config.passwd)
    # stdin,stdout,stderr=s.exec_command('/root/test.sh')
    stdin, stdout, stderr = s.exec_command('cd gongfangautotest/chengsheng;'
                                           'python 24_judge_create_wgxwkf-attack-and-victim.py')
    out = stdout.readlines()
    print(out)
    check = ['登陆成功\n', '添加攻击队违规行为处置成功\n', '登陆成功\n', '添加防守队违规行为处置成功\n']
    assert out == check
    s.close()
