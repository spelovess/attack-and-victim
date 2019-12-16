#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import config


def test_admin_distribute_report_and_attacker_check_report_status():
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=config.localhost, port=config.port, username=config.user, password=config.passwd)
    # stdin,stdout,stderr=s.exec_command('/root/test.sh')
    stdin, stdout, stderr = s.exec_command('cd gongfangautotest/chengsheng;'
                                           'pyresttest ' + config.remotehost + ' 08_new_admin_distribute_'
                                           'report_attack_check-report-status.yaml --skip_term_colors')
    out = stdout.readlines()
    print(out)
    check = ['Test Group admin-distribute-attack-report-and-check-report-status'
             ' SUCCEEDED: : 6/6 Tests Passed!\n']
    assert out == check
    s.close()
