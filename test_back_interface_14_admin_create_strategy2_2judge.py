#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import config


def test_admin_create_strategy2():
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=config.localhost, port=config.port, username=config.user, password=config.passwd)
    # stdin,stdout,stderr=s.exec_command('/root/test.sh')
    stdin, stdout, stderr = s.exec_command('cd gongfangautotest/chengsheng;'
                                           'pyresttest ' + config.remotehost + ' 14_new_admin_create'
                                                                               '_strategy_2judge.yaml '
                                                                               '--skip_term_colors')
    out = stdout.readlines()
    print(out)
    check = ['Test Group admin-create-strategy2 SUCCEEDED: : 7/7 Tests Passed!\n']
    assert out == check
    s.close()
