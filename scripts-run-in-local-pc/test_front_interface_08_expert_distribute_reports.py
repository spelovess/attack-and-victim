# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import config

browser = webdriver.Chrome()


# 用户登陆
def test_login():
    browser.get(config.remotehost + '/#/login')
    time.sleep(1)
    yhm = browser.find_element_by_xpath('//*[@id="app"]/div/div/form/div[1]/div/div[1]/input')
    yhm.send_keys('cs_expert')  # 用户名
    time.sleep(1)
    mm = browser.find_element_by_xpath('//*[@id="app"]/div/div/form/div[2]/div/div[1]/input')
    mm.send_keys('Admin123')  # 密码
    time.sleep(1)
    yzm = browser.find_element_by_xpath('//*[@id="app"]/div/div/form/div[3]/div/div[1]/input')
    yzm.send_keys('xxx')  # 验证码
    time.sleep(1)
    dl = browser.find_element_by_xpath('//*[@id="app"]/div/div/form/div[4]/div/button')
    dl.click()
    time.sleep(1)
    assert 0 == 0


# 攻击方成绩分发
def test_ffgjcj():
    browser.get(config.remotehost + '/#/page/score/attack')
    time.sleep(1)
    ck1 = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[1]/div[2]/div[1]/div[3]/table/'
        'tbody/tr[1]/td[11]/div/button[2]/span')
    ck1.click()  # 点击分配
    time.sleep(3)
    psgjcj = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[4]/div/div/div[2]/div[1]/'
        'div/label[1]/span[1]/span')
    psgjcj.click()  # 点击裁判1
    time.sleep(1)
    psgjcj = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[4]/div/div/div[2]/div[1]/d'
        'iv/label[2]/span[1]/span')
    psgjcj.click()  # 点击裁判2
    time.sleep(1)
    tg = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[4]/div/div/div[2]/div[2]/button[1]/span')
    tg.click()  # 点击确定
    time.sleep(1)
    assert 0 == 0


# 防守方成绩分发
def test_fffscj():
    browser.get(config.remotehost + '/#/page/score/defense')
    time.sleep(1)
    ck1 = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[1]/div[2]/div[1]/div[3]/table/'
        'tbody/tr[1]/td[11]/div/button[2]/span')
    ck1.click()  # 点击分配
    time.sleep(3)
    psgjcj = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[4]/div/div/div[2]/div[1]/d'
        'iv/label[1]/span[1]/span')
    psgjcj.click()  # 点击裁判1
    time.sleep(1)
    psgjcj = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[4]/div/div/div[2]/div[1]/div/'
        'label[2]/span[1]/span')
    psgjcj.click()  # 点击裁判2
    time.sleep(1)
    tg = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[4]/div/div/div[2]/div[2]/button[1]/span')
    tg.click()  # 点击确定
    time.sleep(1)
    assert 0 == 0
    browser.close()
