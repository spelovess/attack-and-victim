# -*- coding: utf-8 -*

import os
import time
from selenium import webdriver

now = time.strftime("%Y%m%d%H%M%S")

#=================================back-interface-test=================================================
os.system('pytest test_back_interface_01_admin_add_pre_config.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_02_attacker_add_3_attack_reports.py --alluredir'
          '=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_03_victimer_add_3_victim_reports.py --alluredir'
          '=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_04_judge_mark_6reports.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_05_admin_check_reports_status.py --alluredir'
          '=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_06_admin_create_stratery_1judge.py --alluredir'
          '=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_07_attacker_add_report.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_08_admin_distribute_report_and_attacker_check_report_status.py '
          '--alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_09_victimer_add_report.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_10_admin_distribute_report_and_victimer_check_report_status.py '
          '--alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_11_expert_mark_report.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_12_admin_check_report_status.py --alluredir'
          '=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_13_admin_delete_strategy1.py --alluredir'
          '=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_14_admin_create_strategy2_2judge.py --alluredir'
          '=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_15_attacker_add_3_attack_reports.py --alluredir'
          '=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_16_victimer_add_3_victim_reports.py --alluredir'
          '=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_17_judge1_mark_6reports.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_18_admin_check_report_status.py --alluredir'
          '=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_19_judge2_mark_6reports.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_20_admin_check_report_status.py --alluredir'
          '=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_21_attacker_create_2gwgjsq.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_22_expert_mark_gwgjsq.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_23_admin_check_gwgjsq_status.py --alluredir'
          '=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_24_judge_create_2gwxwkf.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_back_interface_25_admin_check_wgxwkf.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_front_interface_02_changepassword.py')
time.sleep(5)
os.system('pytest test_back_interface_deletedate.py')
time.sleep(5)

##=================================================front-interface-test================================================
browser = webdriver.Chrome()
running = True
os.system('pytest test_front_interface_01_admin_add_pre_config.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_front_interface_02_changepassword.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_front_interface_03_attacker_add_3_reports.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_front_interface_04_victimer_add_3_reports.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_front_interface_05_judge1_mark_6_reports.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_front_interface_06_judge2_mark_6_reports.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_front_interface_07_create_strategy_judge_1.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_front_interface_03_attacker_add_3_reports.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_front_interface_04_victimer_add_3_reports.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_front_interface_08_expert_distribute_reports.py --alluredir'
          '=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_front_interface_08_expert_mark_report.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_front_interface_09_delete_strategy1.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_front_interface_13_attacker_create_2_gwgjsq.py --alluredir'
          '=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_front_interface_13_attacker_create_2_gwgjsq.py --alluredir'
          '=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_front_interface_14_expert_mark_gwgjsq.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_front_interface_15_gudge_create_gjwgxwcz.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('pytest test_front_interface_16_gudge_create_fswgxwcz.py --alluredir=./allure-results-' + now)
time.sleep(5)
os.system('allure generate allure-results-' + now + ' -o allure-report-' + now + '\html-' + now)
time.sleep(5)
os.system('pytest test_back_interface_deletedate.py')
