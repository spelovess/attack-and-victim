#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import config


def test_judge1_mark_6reports():
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=config.localhost, port=config.port, username=config.user, password=config.passwd)
    # stdin,stdout,stderr=s.exec_command('/root/test.sh')
    stdin, stdout, stderr = s.exec_command('cd gongfangautotest/chengsheng;'
                                           'pyresttest ' + config.remotehost + ' 17_new_judge1'
                                                                               '_6reports_attackandvictim.yaml'
                                                                               ' --skip_term_colors')
    out = stdout.readlines()
    print(out)
    check = ['Test Group judge1-mark-report-strategy2 SUCCEEDED: : 10/10 Tests Passed!\n']
    assert out == check
    s.close()
