#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import config


def test_add_pre_config():
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=config.localhost, port=config.port, username=config.user, password=config.passwd)
    # stdin,stdout,stderr=s.exec_command('/root/test.sh')
    stdin, stdout, stderr = s.exec_command('cd gongfangautotest/chengsheng;'
                                           'pyresttest ' + config.remotehost + ' 01_new_admin_add_pre_config.yaml'
                                                                               ' --skip_term_colors')
    out = stdout.readlines()
    print(out)
    check = ['Test Group pre-configuration SUCCEEDED: : 18/18 Tests Passed!\n']
    assert out == check
    s.close()
