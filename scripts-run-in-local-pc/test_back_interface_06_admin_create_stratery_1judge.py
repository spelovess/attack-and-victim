#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import config


def test_admin_create_stratery_1judge():
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=config.localhost, port=config.port, username=config.user, password=config.passwd)
    # stdin,stdout,stderr=s.exec_command('/root/test.sh')
    stdin, stdout, stderr = s.exec_command('cd gongfangautotest/chengsheng;'
                                           'pyresttest ' + config.remotehost + ' 06_new_admin_create_strategy'
                                                                               '_1judge.yaml --skip_term_colors')
    out = stdout.readlines()
    print(out)
    check = ['Test Group admin-create-strategy1 SUCCEEDED: : 7/7 Tests Passed!\n']
    assert out == check
    s.close()
