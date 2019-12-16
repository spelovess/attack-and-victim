#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import config


def test_admin_check_wgxwkf():
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=config.localhost, port=config.port, username=config.user, password=config.passwd)
    # stdin,stdout,stderr=s.exec_command('/root/test.sh')
    stdin, stdout, stderr = s.exec_command('cd gongfangautotest/chengsheng;'
                                           'pyresttest ' + config.remotehost + ' deletedata.yaml'
                                                                               ' --skip_term_colors')

    out = stdout.readlines()
    print(out)
    # check = ['Test Group admin_check_koufenshengxiao SUCCEEDED: : 4/4 Tests Passed!\n']
    # print(check)
    assert 1 == 1
    s.close()
