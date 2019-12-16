# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import os
import config

browser = webdriver.Chrome()


# 攻击方用户登录系统
def test_login():
    # 用户名 密码
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


def test_gwgjsq():
    browser.get(config.remotehost + '/#/page/highRisk')
    time.sleep(3)
    add = browser.find_element_by_xpath('//*[@id="app"]/section/section/main/'
                                        'div/div[1]/div[1]/div[2]/button/span')
    add.click()
    time.sleep(5)  # 点击新增申请
    mbfs = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[1]/div/div/di'
                                         'v[1]/input')
    mbfs.click()
    time.sleep(1)  # 点击目标防守队
    xz = browser.find_element_by_xpath('/html/body/div[5]/div/div/ul/li/span')
    xz.click()
    time.sleep(1)  # 选择目标防守队点击确定
    mbxt = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[2]/div/div[1]/input')
    mbxt.send_keys('系统一')
    time.sleep(1)  # 输入目标系统
    mubiaoip = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[3]/div/div[1]/input')
    mubiaoip.send_keys('1.1.1.1')
    time.sleep(1)  # 输入目标IP
    mubiaourl = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[4]/div/div[1]/input')
    mubiaourl.send_keys('http://adsf.asdf.asdf')
    time.sleep(1)  # 输入目标URL
    gjlx = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[5]/div/div/div[1]/input')
    gjlx.click()
    time.sleep(1)  # 点击攻击类型
    xzlx = browser.find_element_by_xpath('/html/body/div[6]/div/div/ul/li[5]/span')
    xzlx.click()
    time.sleep(1)  # 选择攻击类型
    sm = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[6]/div/div[1]/textarea')
    sm.send_keys('攻击说明一')
    time.sleep(1)  # 输入攻击说明
    picture = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[7]/div/div'
                                            '/label/input')
    picture.send_keys(os.path.abspath('pic1.png'))
    time.sleep(1)  # 上传图片
    ve = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/div/button[1]/span')
    ve.click()
    time.sleep(1)
    assert 0 == 0
    browser.close()
