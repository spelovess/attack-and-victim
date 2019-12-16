# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import os
import config

browser = webdriver.Chrome()
time.sleep(1)


def test_login():
    time.sleep(1)
    browser.get(config.remotehost)
    time.sleep(1)
    username = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/input')
    username.clear()
    username.send_keys('cs_attacker')  # 输入用户名
    time.sleep(1)
    password = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/input')
    password.clear()
    password.send_keys('Admin123')  # 输入密码
    time.sleep(1)
    ver = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[3]/div/div/input')
    password.clear()
    ver.send_keys('x')  # 输入验证码
    time.sleep(1)
    login = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div/button')
    login.click()
    time.sleep(1)
    assert 0 == 0


def test_attack_submit_grade():  # 路径可优化，
    # 防守单位第几个，目标IP，目标系统，url，攻击类型第几个，说明，成绩图片，文件
    time.sleep(1)
    browser.get(config.remotehost + '/#/page/score')
    time.sleep(1)
    submit_grade = browser.find_element_by_xpath('//*[@id="app"]/section/section/main/div/'
                                                 'div[1]/div[2]/button[1]/span')
    submit_grade.click()  # 点击提交成绩
    time.sleep(5)
    victim = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/form/div[1'
                                           ']/div/div/div[1]/input')
    victim.click()  # 点击防守队
    time.sleep(1)
    victim_team = browser.find_element_by_xpath('/html/body/div[7]/div/div/ul/li/span')
    victim_team.click()  # 选择防守队
    time.sleep(1)
    victim_ip = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/form/div[2]/div/div[1]/input')
    victim_ip.send_keys('1.1.1.1')
    time.sleep(1)  # 输入目标IP
    victim_system = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/form/div[3]/d'
                                                  'iv/div[1]/input')
    victim_system.send_keys('系统二')  # 输入目标系统
    time.sleep(1)
    url = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/form/div[4]/div/div[1]/input')
    url.send_keys('http://asdf.asdf.asdf')  # 输入目标url
    time.sleep(1)
    attacktype = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/form/div[5]/div/div'
                                               '/div[1]/input')
    attacktype.click()  # 点击攻击类型
    time.sleep(1)
    attack_type = browser.find_element_by_xpath('/html/body/div[8]/div/div/ul/li[6]')
    attack_type.click()  # 选择攻击类型
    time.sleep(1)
    attackip = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/form/div[6]/div/div/'
                                             'div[1]/input')
    attackip.click()  # 点击攻击出口IP
    time.sleep(1)
    attack_ip = browser.find_element_by_xpath('/html/body/div[9]/div/div/ul/li[1]/span')
    attack_ip.click()
    time.sleep(1)  # 选择攻击出口IP
    tool = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/form/div[7]/di'
                                         'v/div[1]/div[1]/p/i')
    tool.click()  # 选择使用工具
    time.sleep(1)
    tool1 = browser.find_element_by_xpath(
        '/html/body/div[5]/div/div/div[2]/form/div[7]/div/div[1]/div[2]/label[1]/span[1]/span')
    tool1.click()
    time.sleep(1)
    wxxq = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/form/div[8]/div/di'
                                         'v[1]/div[1]/p/i')
    wxxq.click()
    time.sleep(1)
    dg = browser.find_element_by_xpath(
        '/html/body/div[5]/div/div/div[2]/form/div[8]/div/div[1]/div[2]/div[1]/span[1]/lab'
        'el/span[1]/span')
    dg.click()
    time.sleep(1)
    num = browser.find_element_by_xpath(
        '/html/body/div[5]/div/div/div[2]/form/div[8]/div/div[1]/div[2]/div[1]/span[2]/div/input')
    num.send_keys(2)  # 输入数量
    time.sleep(1)
    description = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/form/div['
                                                '9]/div/div[1]/textarea')
    description.send_keys('说明一')  # 输入成果说明
    time.sleep(1)
    image = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/form/div[10]'
                                          '/div/div/label/input')
    image.send_keys(os.path.abspath('pic1.png'))
    time.sleep(1)
    documents = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/form/div[11]'
                                              '/div/button/span')
    documents.click()
    time.sleep(1)
    documents = browser.find_element_by_xpath('//*[@id="fileUpload"]/div[1]/input')
    documents.send_keys(os.path.abspath('攻击方成果报告.docx'))
    time.sleep(1)
    confirm = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/div/button[1]/span')
    confirm.click()
    time.sleep(1)
    assert 0 == 0
    browser.close()
