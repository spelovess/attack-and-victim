#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import config


def test_admin_check_gwgjsq_status():
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=config.localhost, port=config.port, username=config.user, password=config.passwd)
    # stdin,stdout,stderr=s.exec_command('/root/test.sh')
    stdin, stdout, stderr = s.exec_command('cd gongfangautotest/chengsheng;'
                                           'pyresttest ' + config.remotehost + ' 23_admin_check_gwgjsq-status.'
                                                                               'yaml --skip_term_colors')
    out = stdout.readlines()
    print(out)
    check = ['Test Group admin_check_gwgjsq-status SUCCEEDED: : 3/3 Tests Passed!\n']
    assert out == check
    s.close()
