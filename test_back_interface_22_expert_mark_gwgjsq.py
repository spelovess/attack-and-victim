#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import config


def test_expert_mark_gwgjsq():
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=config.localhost, port=config.port, username=config.user, password=config.passwd)
    # stdin,stdout,stderr=s.exec_command('/root/test.sh')
    stdin, stdout, stderr = s.exec_command('cd gongfangautotest/chengsheng;'
                                           'pyresttest ' + config.remotehost + ' 22_new_expert_'
                                                                               'gwgjsq.yaml --skip_term_colors')
    out = stdout.readlines()
    print(out)
    check = ['Test Group expert_mark_gwgjsq SUCCEEDED: : 5/5 Tests Passed!\n']
    assert out == check
    s.close()
