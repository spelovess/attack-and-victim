# -*- coding: utf-8 -*-

from selenium import webdriver
import os
import time
import config

browser = webdriver.Chrome()


# 用户登陆
def test_login1():
    browser.get(config.remotehost + '/#/login')
    time.sleep(1)
    yhm = browser.find_element_by_xpath('//*[@id="app"]/div/div/form/div[1]/div/div[1]/input')
    yhm.send_keys('cs_judge1')  # 用户名
    time.sleep(1)
    mm = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div[1]/input')
    mm.send_keys('Admin123')  # 密码
    time.sleep(1)
    yzm = browser.find_element_by_xpath('//*[@id="app"]/div/div/form/div[3]/div/div[1]/input')
    yzm.send_keys('sss')  # 验证码
    time.sleep(1)
    dl = browser.find_element_by_xpath('//*[@id="app"]/div/div/form/div[4]/div/button')
    dl.click()
    time.sleep(1)
    assert 0 == 0


# 创建攻击队处置扣分
def test_wgxw1():
    browser.get(config.remotehost + '/#/page/disposal')
    time.sleep(3)
    xjcz = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div/div[2]/div[1]/div/div[1]/div[2]/button')
    xjcz.click()  # 新建处置
    time.sleep(3)
    wgdw = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div[2]/div[1]/div/div[4]/div/div/d'
        'iv[2]/form/div[1]/div/div/div[1]/input')
    wgdw.click()  # 违规队伍
    time.sleep(5)
    chdw = browser.find_element_by_xpath('/html/body/div[4]/div/div/ul/li/span')
    chdw.click()  # 选择违规的队伍
    time.sleep(1)
    wgtime = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div[2]/div[1]/div/div[4]/div/div/di'
        'v[2]/form/div[2]/div/div[1]/input')
    wgtime.click()  # 违规时间
    time.sleep(1)
    chtime = browser.find_element_by_xpath(
        '/html/body/div[5]/div[1]/div/div/div[3]/table[1]/tbody/tr[6]/td[2]/div/span')
    chtime.click()  # 选择违规时间
    time.sleep(1)
    qr = browser.find_element_by_xpath('/html/body/div[5]/div[2]/button')
    qr.click()  # 点击确定
    time.sleep(1)
    kf = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div[2]/div[1]/div/div[4]/div/div/div[2]/'
        'form/div[3]/div/div[1]/input')
    kf.send_keys(222)  # 扣分
    time.sleep(1)
    wgsm = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div[2]/div[1]/div/div[4]/div/div/div[2]/f'
        'orm/div[4]/div/div[1]/textarea')
    wgsm.send_keys('说明一')  # 违规行为说明
    time.sleep(1)
    scwj = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div[2]/div[1]/div/div[4]/div/div/div[2]/f'
        'orm/div[5]/div/div[1]/input')
    scwj.send_keys(os.path.abspath('攻击方成果报告.docx'))  # 点击上传文件
    time.sleep(1)
    qd1 = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div[2]/div[1]/div/div[4]/div/div/div[3]/d'
        'iv/button[1]/span')
    qd1.click()  # 确定
    time.sleep(1)
    qd2 = browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div/div[3]/button[1]')
    qd2.click()
    time.sleep(2)
    assert 0 == 0
    browser.close()
