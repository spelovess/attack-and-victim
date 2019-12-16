# -*- coding: utf-8 -*-

from selenium import webdriver
import os
import time
import config

browser = webdriver.Chrome()


def test_login2():
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


# 创建防守队处置扣分
def test_fskf2():
    browser.get(config.remotehost + '/#/page/disposal')
    time.sleep(3)
    fscz = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div/div[1]/div/div/div/div[1]/div[3]/div')
    fscz.click()  # 点击防守队伍处置
    time.sleep(3)
    xjcz2 = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div/div[2]/div[2]/div/div[1]/div[2]/button')
    xjcz2.click()  # 点击新建处置
    time.sleep(5)
    wgdw2 = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div[2]/div[2]/div/div[4]/div/div/'
        'div[2]/form/div[1]/div/div/div[1]/input')
    wgdw2.click()  # 违规队伍
    time.sleep(1)
    chwgdw = browser.find_element_by_xpath('/html/body/div[4]/div/div/ul/li/span')
    chwgdw.click()  # 选择违规队伍
    time.sleep(1)
    wgtm = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div[2]/div[2]/div/div[4]/div/div/di'
        'v[2]/form/div[2]/div/div[1]/input')
    wgtm.click()  # 违规时间
    time.sleep(1)
    cf = browser.find_element_by_xpath('/html/body/div[5]/div[2]/a')
    cf.click()  # 确定
    time.sleep(1)
    kf2 = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div[2]/div[2]/div/div[4]/div/div/div'
        '[2]/form/div[3]/div/div[1]/input')
    kf2.send_keys(222)
    time.sleep(1)
    wgdt = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div[2]/div[2]/div/div[4]/div/div/div['
        '2]/form/div[4]/div/div[1]/textarea')
    wgdt.send_keys('说明一')  # 违规成果说明
    time.sleep(1)
    scfj2 = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div[2]/div[2]/div/div[4]/div/div/div['
        '2]/form/div[5]/div/div[1]/input')
    scfj2.send_keys(os.path.abspath('攻击方成果报告.docx'))  # 上传文件
    time.sleep(1)
    cf1 = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div[2]/div[2]/div/div[4]/div/div/di'
        'v[3]/div/button[1]/span')
    cf1.click()
    time.sleep(1)
    cf2 = browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div/div[3]/button[1]/span')
    cf2.click()
    time.sleep(1)
    assert 0 == 0
    browser.close()
